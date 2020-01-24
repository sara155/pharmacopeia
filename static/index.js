(function evaluate(require, module, exports, process, setImmediate, global, __dirname, __filename) {"use strict";

var _printJs = require("print-js");

var _printJs2 = _interopRequireDefault(_printJs);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function printTest() {
  (0, _printJs2.default)({
    printable: "app",
    type: "html",
    style: ".result {visibility: visible;font-size: 30px;color: green;}",
    css: "{{ url_for('static', filename='print.css') }}",
    onPrintDialogClose: printJobComplete
  });
}

function printJobComplete() {
  alert("print job complete");
}

document.getElementById("test-button").addEventListener("click", printTest);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9zcmMvaW5kZXguanMiXSwibmFtZXMiOlsicHJpbnRUZXN0IiwicHJpbnRhYmxlIiwidHlwZSIsInN0eWxlIiwiY3NzIiwib25QcmludERpYWxvZ0Nsb3NlIiwicHJpbnRKb2JDb21wbGV0ZSIsImFsZXJ0IiwiZG9jdW1lbnQiLCJnZXRFbGVtZW50QnlJZCIsImFkZEV2ZW50TGlzdGVuZXIiXSwibWFwcGluZ3MiOiI7O0FBQUE7Ozs7OztBQUVBLFNBQVNBLFNBQVQsR0FBcUI7QUFDbkIseUJBQVE7QUFDTkMsZUFBVyxLQURMO0FBRU5DLFVBQU0sTUFGQTtBQUdOQyxXQUFPLDZEQUhEO0FBSU5DLFNBQUssZUFKQztBQUtOQyx3QkFBb0JDO0FBTGQsR0FBUjtBQU9EOztBQUVELFNBQVNBLGdCQUFULEdBQTRCO0FBQzFCQyxRQUFNLG9CQUFOO0FBQ0Q7O0FBRURDLFNBQVNDLGNBQVQsQ0FBd0IsYUFBeEIsRUFBdUNDLGdCQUF2QyxDQUF3RCxPQUF4RCxFQUFpRVYsU0FBakUiLCJmaWxlIjoiaW5kZXguanMiLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgcHJpbnRKUyBmcm9tIFwicHJpbnQtanNcIjtcblxuZnVuY3Rpb24gcHJpbnRUZXN0KCkge1xuICBwcmludEpTKHtcbiAgICBwcmludGFibGU6IFwiYXBwXCIsXG4gICAgdHlwZTogXCJodG1sXCIsXG4gICAgc3R5bGU6IFwiLnJlc3VsdCB7dmlzaWJpbGl0eTogdmlzaWJsZTtmb250LXNpemU6IDMwcHg7Y29sb3I6IGdyZWVuO31cIixcbiAgICBjc3M6IFwic3JjL3N0eWxlLmNzc1wiLFxuICAgIG9uUHJpbnREaWFsb2dDbG9zZTogcHJpbnRKb2JDb21wbGV0ZVxuICB9KTtcbn1cblxuZnVuY3Rpb24gcHJpbnRKb2JDb21wbGV0ZSgpIHtcbiAgYWxlcnQoXCJwcmludCBqb2IgY29tcGxldGVcIik7XG59XG5cbmRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwidGVzdC1idXR0b25cIikuYWRkRXZlbnRMaXN0ZW5lcihcImNsaWNrXCIsIHByaW50VGVzdCk7XG4iXX0=
//# sourceURL=https://r71k74qq7m.csb.app/src/index.js
})