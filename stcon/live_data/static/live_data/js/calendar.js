"use strict";


function createCalendar(elem, year, month, day) {

    let mon = month - 1; // месяцы в JS идут от 0 до 11, а не от 1 до 12
    let d = new Date(year, mon);

    let list_month = {
        0: "January",
        1: "February",
        2: "March",
        3: "April",
        4: "May",
        5: "June",
        6: "July",
        7: "August",
        8: "September",
        9: "October",
        10: "November",
        11: "December"
    };
    let m = d.getMonth().toString();
    let month_name = list_month[m];




    // html code in let table:

    let table = `

<div class="card ">
<a name="calendar"></a>
<h5 class="card-header">Select start date</h5>
<div class="card-body">
  <!-- <h6 class="card-title">March</h6> -->

  <select class="form-select" id="inputGroupSelect01">
    <option selected>Choose...</option>
    <option value="1">Potencial P1, Volt</option>
    <option value="2">Voltage V, Volt</option>
    <option value="3">Carent A, Amper</option>
  </select>

  <div class="btn-group dropend">
    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
      ${month_name}
    </button>

    <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1" id="list_month_left">
      <li><a class="dropdown-item" href="##" data-command="1">January</a></li>
      <li><a class="dropdown-item" href="##" data-command="2">February</a></li>
      <li><a class="dropdown-item" href="##" data-command="3">March</a></li>
      <li><a class="dropdown-item" href="##" data-command="4">April</a></li>
      <li><a class="dropdown-item" href="##" data-command="5">May</a></li>
      <li><a class="dropdown-item" href="##" data-command="6">June</a></li>
      <li><a class="dropdown-item" href="##" data-command="7">July</a></li>
      <li><a class="dropdown-item" href="##" data-command="8">August</a></li>
      <li><a class="dropdown-item" href="##" data-command="9">September</a></li>
      <li><a class="dropdown-item" href="##" data-command="10">October</a></li>
      <li><a class="dropdown-item" href="##" data-command="11">November</a></li>
      <li><a class="dropdown-item" href="##" data-command="12">December</a></li>
    </ul>

    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton2" data-bs-toggle="dropdown" aria-expanded="false">
      ${year}
    </button>
    <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton2" id="list_year_left">
      <li><a class="dropdown-item" href="##" data-command="2015">2015</a></li>
      <li><a class="dropdown-item" href="##" data-command="2016">2016</a></li>
      <li><a class="dropdown-item" href="##" data-command="2017">2017</a></li>
      <li><a class="dropdown-item" href="##" data-command="2018">2018</a></li>
      <li><a class="dropdown-item" href="##" data-command="2019">2019</a></li>
      <li><a class="dropdown-item" href="##" data-command="2020">2020</a></li>
      <li><a class="dropdown-item" href="##" data-command="2021">2021</a></li>
      <li><a class="dropdown-item" href="##" data-command="2022">2022</a></li>
      <li><a class="dropdown-item" href="##" data-command="2023">2023</a></li>
      <li><a class="dropdown-item" href="##" data-command="2024">2024</a></li>
      <li><a class="dropdown-item" href="##" data-command="2025">2025</a></li>
      <li><a class="dropdown-item" href="##" data-command="2026">2026</a></li>
      <li><a class="dropdown-item" href="##" data-command="2027">2027</a></li>
      <li><a class="dropdown-item" href="##" data-command="2028">2028</a></li>
      <li><a class="dropdown-item" href="##" data-command="2029">2029</a></li>
      <li><a class="dropdown-item" href="##" data-command="2030">2030</a></li>
      <li><a class="dropdown-item" href="##" data-command="2031">2031</a></li>
      <li><a class="dropdown-item" href="##" data-command="2032">2032</a></li>
    </ul>         
  </div>




  <div class="table-responsive">
    <table class="table table-bordered text-center">
      <thead>
        <tr class="table-info">
          <th scope="col">Mo</th>
          <th scope="col">Tu</th>
          <th scope="col">We</th>
          <th scope="col">Th</th>
          <th scope="col">Fr</th>
          <th scope="col">Sa</th>
          <th scope="col">Su</th>
        </tr>
      </thead>
      <tbody id="list_days_left">
        <tr>
`;

    let table_end = `
</tr>
</tbody>
</table>
</div>

<p class="card-text">Starting point of the time period.</p>
<a href="#grafic" class="btn btn-secondary" id="button_summary_left">Show line chart</a>
</div>
</div>
`;





    // пробелы для первого ряда
    // с понедельника до первого дня месяца
    // * * * 1  2  3  4
    for (let i = 0; i < getDay(d); i++) {
        table += '<td></td>';
    }

    let active_day = '';
    // <td> ячейки календаря с датами
    while (d.getMonth() == mon) {

        if(d.getDate() == day) active_day = 'class="table-active"';
        else active_day = '';

        table += `<td data-command="${d.getDate()}" ${active_day}>` + d.getDate() + '</td>';

        if (getDay(d) % 7 == 6) { // вс, последний день - перевод строки
            table += '</tr><tr>';
        }

        d.setDate(d.getDate() + 1);
    }

    // добить таблицу пустыми ячейками, если нужно
    // 29 30 31 * * * *
    if (getDay(d) != 0) {
        for (let i = getDay(d); i < 7; i++) {
            table += '<td></td>';
        }
    }

    // закрыть таблицу
    table += table_end;

    elem.innerHTML = table;

    list_days_left = document.getElementById("list_days_left");
    list_days_left.addEventListener("click", select_day);

    list_month_left = document.getElementById("list_month_left");
    list_month_left.addEventListener("click", select_month);

    list_year_left = document.getElementById("list_year_left");
    list_year_left.addEventListener("click", select_year);

    button_summary_left = document.getElementById("button_summary_left");
    button_summary_left.addEventListener("click", send_button_left);


}

function getDay(date) { // получить номер дня недели, от 0 (пн) до 6 (вс)
    let day = date.getDay();
    if (day == 0) day = 7; // сделать воскресенье (0) последним днем
    return day - 1;
}




let cal_left = document.getElementById("calendar_left");
let date_now = new Date();

let list_days_left;
let list_month_left;
let list_year_left;
let button_summary_left;
let day_left = date_now.getDate();
let month_left = date_now.getMonth() + 1;
let year_left = date_now.getFullYear();
createCalendar(cal_left, year_left, month_left, day_left);




function select_day(event) {

  let a = event.target.closest("td");
  if (a == null) return;

  let act = a.dataset.command;
  if (act == undefined) return;

  day_left = +act;

  createCalendar(cal_left, year_left, month_left, day_left);
}

function select_month(event) {

    let a = event.target.closest("a");
    if (a == null) return;

    let act = a.dataset.command;
    if (act == undefined) return;

    month_left = +act;

    createCalendar(cal_left, year_left, month_left, day_left);
}

function select_year(event) {

    let a = event.target.closest("a");
    if (a == null) return;

    let act = a.dataset.command;
    if (act == undefined) return;

    year_left = +act;

    createCalendar(cal_left, year_left, month_left, day_left);
}






// ----------------------------------------------------------------------------------------
// calendar right
// ----------------------------------------------------------------------------------------



function createCalendarRight(elem, year, month, day) {

  let mon = month - 1; // месяцы в JS идут от 0 до 11, а не от 1 до 12
  let d = new Date(year, mon);

  let list_month = {
      0: "January",
      1: "February",
      2: "March",
      3: "April",
      4: "May",
      5: "June",
      6: "July",
      7: "August",
      8: "September",
      9: "October",
      10: "November",
      11: "December"
  };
  let m = d.getMonth().toString();
  let month_name = list_month[m];




  // html code in let table:

  let table = `

<div class="card ">
<a name="calendar"></a>
<h5 class="card-header">Select next date</h5>
<div class="card-body">
<!-- <h6 class="card-title">March</h6> -->

<select class="form-select" id="inputGroupSelect01">
  <option selected>Choose...</option>
  <option value="1">Potencial P1, Volt</option>
  <option value="2">Voltage V, Volt</option>
  <option value="3">Carent A, Amper</option>
</select>

<div class="btn-group dropend">
  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
    ${month_name}
  </button>

  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1" id="list_month_right">
    <li><a class="dropdown-item" href="##" data-command="1">January</a></li>
    <li><a class="dropdown-item" href="##" data-command="2">February</a></li>
    <li><a class="dropdown-item" href="##" data-command="3">March</a></li>
    <li><a class="dropdown-item" href="##" data-command="4">April</a></li>
    <li><a class="dropdown-item" href="##" data-command="5">May</a></li>
    <li><a class="dropdown-item" href="##" data-command="6">June</a></li>
    <li><a class="dropdown-item" href="##" data-command="7">July</a></li>
    <li><a class="dropdown-item" href="##" data-command="8">August</a></li>
    <li><a class="dropdown-item" href="##" data-command="9">September</a></li>
    <li><a class="dropdown-item" href="##" data-command="10">October</a></li>
    <li><a class="dropdown-item" href="##" data-command="11">November</a></li>
    <li><a class="dropdown-item" href="##" data-command="12">December</a></li>
  </ul>

  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton2" data-bs-toggle="dropdown" aria-expanded="false">
    ${year}
  </button>
  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton2" id="list_year_right">
    <li><a class="dropdown-item" href="##" data-command="2015">2015</a></li>
    <li><a class="dropdown-item" href="##" data-command="2016">2016</a></li>
    <li><a class="dropdown-item" href="##" data-command="2017">2017</a></li>
    <li><a class="dropdown-item" href="##" data-command="2018">2018</a></li>
    <li><a class="dropdown-item" href="##" data-command="2019">2019</a></li>
    <li><a class="dropdown-item" href="##" data-command="2020">2020</a></li>
    <li><a class="dropdown-item" href="##" data-command="2021">2021</a></li>
    <li><a class="dropdown-item" href="##" data-command="2022">2022</a></li>
    <li><a class="dropdown-item" href="##" data-command="2023">2023</a></li>
    <li><a class="dropdown-item" href="##" data-command="2024">2024</a></li>
    <li><a class="dropdown-item" href="##" data-command="2025">2025</a></li>
    <li><a class="dropdown-item" href="##" data-command="2026">2026</a></li>
    <li><a class="dropdown-item" href="##" data-command="2027">2027</a></li>
    <li><a class="dropdown-item" href="##" data-command="2028">2028</a></li>
    <li><a class="dropdown-item" href="##" data-command="2029">2029</a></li>
    <li><a class="dropdown-item" href="##" data-command="2030">2030</a></li>
    <li><a class="dropdown-item" href="##" data-command="2031">2031</a></li>
    <li><a class="dropdown-item" href="##" data-command="2032">2032</a></li>
  </ul>         
</div>




<div class="table-responsive">
  <table class="table table-bordered text-center">
    <thead>
      <tr class="table-info">
        <th scope="col">Mo</th>
        <th scope="col">Tu</th>
        <th scope="col">We</th>
        <th scope="col">Th</th>
        <th scope="col">Fr</th>
        <th scope="col">Sa</th>
        <th scope="col">Su</th>
      </tr>
    </thead>
    <tbody id="list_days_right">
      <tr>
`;

  let table_end = `
</tr>
</tbody>
</table>
</div>

<p class="card-text">Time period end point.</p>
<a href="#grafic" class="btn btn-secondary" id="button_summary_right">Show line chart</a>
</div>
</div>
`;





  // пробелы для первого ряда
  // с понедельника до первого дня месяца
  // * * * 1  2  3  4
  for (let i = 0; i < getDay(d); i++) {
      table += '<td></td>';
  }

  let active_day = '';
  // <td> ячейки календаря с датами
  while (d.getMonth() == mon) {

      if(d.getDate() == day) active_day = 'class="table-active"';
      else active_day = '';

      table += `<td data-command="${d.getDate()}" ${active_day}>` + d.getDate() + '</td>';

      if (getDay(d) % 7 == 6) { // вс, последний день - перевод строки
          table += '</tr><tr>';
      }

      d.setDate(d.getDate() + 1);
  }

  // добить таблицу пустыми ячейками, если нужно
  // 29 30 31 * * * *
  if (getDay(d) != 0) {
      for (let i = getDay(d); i < 7; i++) {
          table += '<td></td>';
      }
  }

  // закрыть таблицу
  table += table_end;

  elem.innerHTML = table;

  list_days_right = document.getElementById("list_days_right");
  list_days_right.addEventListener("click", select_day_right);

  list_month_right = document.getElementById("list_month_right");
  list_month_right.addEventListener("click", select_month_right);

  list_year_right = document.getElementById("list_year_right");
  list_year_right.addEventListener("click", select_year_right);

  button_summary_right = document.getElementById("button_summary_right");
  button_summary_right.addEventListener("click", send_button_left);


}

// function getDay(date) { // получить номер дня недели, от 0 (пн) до 6 (вс)
//   let day = date.getDay();
//   if (day == 0) day = 7; // сделать воскресенье (0) последним днем
//   return day - 1;
// }




let cal_right = document.getElementById("calendar_right");

let list_days_right;
let list_month_right;
let list_year_right;
let button_summary_right;
let day_right = date_now.getDate();
let month_right = date_now.getMonth() + 1;
let year_right = date_now.getFullYear();
createCalendarRight(cal_right, year_right, month_right, day_right);




function select_day_right(event) {

let a = event.target.closest("td");
if (a == null) return;

let act = a.dataset.command;
if (act == undefined) return;

day_right = +act;

createCalendarRight(cal_right, year_right, month_right, day_right);
}

function select_month_right(event) {

  let a = event.target.closest("a");
  if (a == null) return;

  let act = a.dataset.command;
  if (act == undefined) return;

  month_right = +act;

  createCalendarRight(cal_right, year_right, month_right, day_right);
}

function select_year_right(event) {

  let a = event.target.closest("a");
  if (a == null) return;

  let act = a.dataset.command;
  if (act == undefined) return;

  year_right = +act;

  createCalendarRight(cal_right, year_right, month_right, day_right);
}



// ------------------------------------------------------------------------------------------
// common function
// ------------------------------------------------------------------------------------------


function send_button_left(event) {

    let formData = new FormData(document.forms.form_calendar_left);
    formData.append("month_left", month_left);
    formData.append("year_left", year_left);
    formData.append("day_left", day_left);
    formData.append("month_right", month_right);
    formData.append("year_right", year_right);
    formData.append("day_right", day_right);

    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/getdata/');
    xhr.responseType = 'json';
    xhr.send(formData);

    document.getElementById("preloader__image").style.display = "block";

    xhr.onload = function () {
        document.getElementById("preloader__image").style.display = "none";
        if (xhr.status != 200) { 
            console.log(`Error ${xhr.status}: ${xhr.statusText}`); 
        } else {
            let obj_response = xhr.response;
            //console.log(obj_response);
            show_data_chart(obj_response);
        }
    };


    xhr.onerror = function () {
        document.getElementById("preloader__image").style.display = "none";
        console.log("Error XMLHttpRequest()");
    };

}




// -----------------------------------------------------------------------------------------
// drow chart data
// -----------------------------------------------------------------------------------------

let chart_data_line = null;
let config_chart_line = null;
let ctx_chart_line = null;
function show_data_chart(obj_response){

  config_chart_line = {
    type: 'line',
    data: {
      datasets: [{
        label: 'Potencial',
        data: obj_response,
        borderColor: 'rgb(75, 192, 192)',
      }]
    },
    options: {
      responsive: true,
      parsing: {
        xAxisKey: 'x',
        yAxisKey: 'y'
      },
      scales: {
        y: {
          suggestedMin: 0,
          suggestedMax: 3,
          title: {
            display: true,
            text: 'Potencial, Volt'
          }
        },
        x: {
          // min: 1,
          // max: 10,
          //offset: true,
          ticks: {
            color: 'blue',
            //stepSize: 0.5
          },
          title: {
            display: true,
            text: 'Date/Time'
          }
        }
      }
    }
  };


  if(chart_data_line){
    chart_data_line.destroy();
  }

  ctx_chart_line = document.getElementById('chart_data_line');
  chart_data_line = new Chart(ctx_chart_line, config_chart_line);
  




}