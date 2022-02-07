class HtmlReportTemplete:
    def __init__(self):
        self.reportTemplete='''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>Test Report</title>
    <link href="assets/style.css" rel="stylesheet" type="text/css"/></head>
  <body onLoad="init()">
    <script>/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this file,
 * You can obtain one at http://mozilla.org/MPL/2.0/. */


function toArray(iter) {
    if (iter === null) {
        return null;
    }
    return Array.prototype.slice.call(iter);
}

function find(selector, elem) { // eslint-disable-line no-redeclare
    if (!elem) {
        elem = document;
    }
    return elem.querySelector(selector);
}

function findAll(selector, elem) {
    if (!elem) {
        elem = document;
    }
    return toArray(elem.querySelectorAll(selector));
}

function sortColumn(elem) {
    toggleSortStates(elem);
    const colIndex = toArray(elem.parentNode.childNodes).indexOf(elem);
    let key;
    if (elem.classList.contains('result')) {
        key = keyResult;
    } else if (elem.classList.contains('links')) {
        key = keyLink;
    } else {
        key = keyAlpha;
    }
    sortTable(elem, key(colIndex));
}

function showAllExtras() { // eslint-disable-line no-unused-vars
    findAll('.col-result').forEach(showExtras);
}

function hideAllExtras() { // eslint-disable-line no-unused-vars
    findAll('.col-result').forEach(hideExtras);
}

function showExtras(colresultElem) {
    const extras = colresultElem.parentNode.nextElementSibling;
    const expandcollapse = colresultElem.firstElementChild;
    extras.classList.remove('collapsed');
    expandcollapse.classList.remove('expander');
    expandcollapse.classList.add('collapser');
}

function hideExtras(colresultElem) {
    const extras = colresultElem.parentNode.nextElementSibling;
    const expandcollapse = colresultElem.firstElementChild;
    extras.classList.add('collapsed');
    expandcollapse.classList.remove('collapser');
    expandcollapse.classList.add('expander');
}

function showFilters() {
    const filterItems = document.getElementsByClassName('filter');
    for (let i = 0; i < filterItems.length; i++)
        filterItems[i].hidden = false;
}

function addCollapse() {
    // Add links for show/hide all
    const resulttable = find('table#results-table');
    const showhideall = document.createElement('p');
    showhideall.innerHTML = '<a href="javascript:showAllExtras()">Show all details</a> / ' +
                            '<a href="javascript:hideAllExtras()">Hide all details</a>';
    resulttable.parentElement.insertBefore(showhideall, resulttable);

    // Add show/hide link to each result
    findAll('.col-result').forEach(function(elem) {
        const collapsed = getQueryParameter('collapsed') || 'Passed';
        const extras = elem.parentNode.nextElementSibling;
        const expandcollapse = document.createElement('span');
        if (extras.classList.contains('collapsed')) {
            expandcollapse.classList.add('expander');
        } else if (collapsed.includes(elem.innerHTML)) {
            extras.classList.add('collapsed');
            expandcollapse.classList.add('expander');
        } else {
            expandcollapse.classList.add('collapser');
        }
        elem.appendChild(expandcollapse);

        elem.addEventListener('click', function(event) {
            if (event.currentTarget.parentNode.nextElementSibling.classList.contains('collapsed')) {
                showExtras(event.currentTarget);
            } else {
                hideExtras(event.currentTarget);
            }
        });
    });
}

function getQueryParameter(name) {
    const match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search);
    return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
}

function init () { // eslint-disable-line no-unused-vars
    resetSortHeaders();

    addCollapse();

    showFilters();

    sortColumn(find('.initial-sort'));

    findAll('.sortable').forEach(function(elem) {
        elem.addEventListener('click',
            function() {
                sortColumn(elem);
            }, false);
    });
}

function sortTable(clicked, keyFunc) {
    const rows = findAll('.results-table-row');
    const reversed = !clicked.classList.contains('asc');
    const sortedRows = sort(rows, keyFunc, reversed);
    /* Whole table is removed here because browsers acts much slower
     * when appending existing elements.
     */
    const thead = document.getElementById('results-table-head');
    document.getElementById('results-table').remove();
    const parent = document.createElement('table');
    parent.id = 'results-table';
    parent.appendChild(thead);
    sortedRows.forEach(function(elem) {
        parent.appendChild(elem);
    });
    document.getElementsByTagName('BODY')[0].appendChild(parent);
}

function sort(items, keyFunc, reversed) {
    const sortArray = items.map(function(item, i) {
        return [keyFunc(item), i];
    });

    sortArray.sort(function(a, b) {
        const keyA = a[0];
        const keyB = b[0];

        if (keyA == keyB) return 0;

        if (reversed) {
            return keyA < keyB ? 1 : -1;
        } else {
            return keyA > keyB ? 1 : -1;
        }
    });

    return sortArray.map(function(item) {
        const index = item[1];
        return items[index];
    });
}

function keyAlpha(colIndex) {
    return function(elem) {
        return elem.childNodes[1].childNodes[colIndex].firstChild.data.toLowerCase();
    };
}

function keyLink(colIndex) {
    return function(elem) {
        const dataCell = elem.childNodes[1].childNodes[colIndex].firstChild;
        return dataCell == null ? '' : dataCell.innerText.toLowerCase();
    };
}

function keyResult(colIndex) {
    return function(elem) {
        const strings = ['Error', 'Failed', 'Rerun', 'XFailed', 'XPassed',
            'Skipped', 'Passed'];
        return strings.indexOf(elem.childNodes[1].childNodes[colIndex].firstChild.data);
    };
}

function resetSortHeaders() {
    findAll('.sort-icon').forEach(function(elem) {
        elem.parentNode.removeChild(elem);
    });
    findAll('.sortable').forEach(function(elem) {
        const icon = document.createElement('div');
        icon.className = 'sort-icon';
        icon.textContent = 'vvv';
        elem.insertBefore(icon, elem.firstChild);
        elem.classList.remove('desc', 'active');
        elem.classList.add('asc', 'inactive');
    });
}

function toggleSortStates(elem) {
    //if active, toggle between asc and desc
    if (elem.classList.contains('active')) {
        elem.classList.toggle('asc');
        elem.classList.toggle('desc');
    }

    //if inactive, reset all other functions and add ascending active
    if (elem.classList.contains('inactive')) {
        resetSortHeaders();
        elem.classList.remove('inactive');
        elem.classList.add('active');
    }
}

function isAllRowsHidden(value) {
    return value.hidden == false;
}

function filterTable(elem) { // eslint-disable-line no-unused-vars
    const outcomeAtt = 'data-test-result';
    const outcome = elem.getAttribute(outcomeAtt);
    const classOutcome = outcome + ' results-table-row';
    const outcomeRows = document.getElementsByClassName(classOutcome);

    for(let i = 0; i < outcomeRows.length; i++){
        outcomeRows[i].hidden = !elem.checked;
    }

    const rows = findAll('.results-table-row').filter(isAllRowsHidden);
    const allRowsHidden = rows.length == 0 ? true : false;
    const notFoundMessage = document.getElementById('not-found-message');
    notFoundMessage.hidden = !allRowsHidden;
}
</script>
    <h1>{Reportname}</h1>
    <p>Report generated on {ReportGenerated}</p>
    
    <h2>Summary</h2>
    <p>{testcasecnt} tests ran in {totalSeconds} seconds. </p>
    <p class="filter" hidden="true">(Un)check the boxes to filter the results.
    </p><input checked="true" class="filter" data-test-result="passed" hidden="true" name="filter_checkbox" onChange="filterTable(this)" type="checkbox"/>
    <span class="passed">{passedcnt} passed</span>, <input checked="true" class="filter" data-test-result="skipped"  hidden="true" name="filter_checkbox" onChange="filterTable(this)" type="checkbox"/>
    <span class="skipped">{skippedcnt} skipped</span>, <input checked="true" class="filter" data-test-result="failed"  hidden="true" name="filter_checkbox" onChange="filterTable(this)" type="checkbox"/>
    <span class="failed">{failedcnt} failed</span>
    <h2>Results</h2>
    <table id="results-table">
      <thead id="results-table-head">
        <tr>
          <th class="sortable result initial-sort" col="result">Result</th>
          <th class="sortable" col="name">Test</th>
          <th class="sortable" col="duration">Duration(in seconds)</th></tr>
        <tr hidden="true" id="not-found-message">
          <th colspan="4">No results found. Try to check the filters</th></tr></thead>
          
      {ts_tbody}</table></body></html>
        '''
        self.cssFile='''body {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 12px;
  /* do not increase min-width as some may use split screens */
  min-width: 800px;
  color: #999;
}

h1 {
  font-size: 24px;
  color: black;
}

h2 {
  font-size: 16px;
  color: black;
}

p {
  color: black;
}

a {
  color: #999;
}

table {
  border-collapse: collapse;
}

/******************************
 * SUMMARY INFORMATION
 ******************************/
#environment td {
  padding: 5px;
  border: 1px solid #E6E6E6;
}
#environment tr:nth-child(odd) {
  background-color: #f6f6f6;
}

/******************************
 * TEST RESULT COLORS
 ******************************/
span.passed,
.passed .col-result {
  color: green;
}

span.skipped,
span.xfailed,
span.rerun,
.skipped .col-result,
.xfailed .col-result,
.rerun .col-result {
  color: orange;
}

span.error,
span.failed,
span.xpassed,
.error .col-result,
.failed .col-result,
.xpassed .col-result {
  color: red;
}

/******************************
 * RESULTS TABLE
 *
 * 1. Table Layout
 * 2. Extra
 * 3. Sorting items
 *
 ******************************/
/*------------------
 * 1. Table Layout
 *------------------*/
#results-table {
  border: 1px solid #e6e6e6;
  color: #999;
  font-size: 12px;
  width: 100%;
}
#results-table th,
#results-table td {
  padding: 5px;
  border: 1px solid #E6E6E6;
  text-align: left;
}
#results-table th {
  font-weight: bold;
}

/*------------------
 * 2. Extra
 *------------------*/
.log {
  background-color: #e6e6e6;
  border: 1px solid #e6e6e6;
  color: black;
  display: block;
  font-family: "Courier New", Courier, monospace;
  height: 230px;
  overflow-y: scroll;
  padding: 5px;
  white-space: pre-wrap;
}
.log:only-child {
  height: inherit;
}

div.image {
  border: 1px solid #e6e6e6;
  float: right;
  height: 240px;
  margin-left: 5px;
  overflow: hidden;
  width: 320px;
}
div.image img {
  width: 320px;
}

div.video {
  border: 1px solid #e6e6e6;
  float: right;
  height: 240px;
  margin-left: 5px;
  overflow: hidden;
  width: 320px;
}
div.video video {
  overflow: hidden;
  width: 320px;
  height: 240px;
}

.collapsed {
  display: none;
}

.expander::after {
  content: " (show details)";
  color: #BBB;
  font-style: italic;
  cursor: pointer;
}

.collapser::after {
  content: " (hide details)";
  color: #BBB;
  font-style: italic;
  cursor: pointer;
}

/*------------------
 * 3. Sorting items
 *------------------*/
.sortable {
  cursor: pointer;
}

.sort-icon {
  font-size: 0px;
  float: left;
  margin-right: 5px;
  margin-top: 5px;
  /*triangle*/
  width: 0;
  height: 0;
  border-left: 8px solid transparent;
  border-right: 8px solid transparent;
}
.inactive .sort-icon {
  /*finish triangle*/
  border-top: 8px solid #E6E6E6;
}
.asc.active .sort-icon {
  /*finish triangle*/
  border-bottom: 8px solid #999;
}
.desc.active .sort-icon {
  /*finish triangle*/
  border-top: 8px solid #999;
}
 '''
        self.tbody_templete='''<tbody class="{tresult} results-table-row"><tr>
          <td class="col-result">{test_result}</td>
          <td class="col-name">{ts_id}</td>
          <td class="col-duration">{duration}</td>
          
        <tr>
          <td class="extra" colspan="4">
            <div class="empty log">No log output captured.</div></td></tr></tbody>
        
        
        '''
