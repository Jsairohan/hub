function save_servicecode(data, call_back){

    $.ajax({
 type: "POST",
 url: "/createhospbillitems/",
 data: JSON.stringify(data),
 contentType: "application/json",
 dataType: "json",
 success: function (data, status) {
//        alert("Data: " + data + "\nStatus: " + status);
        call_back(data,status);
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log( XMLHttpRequest.responseText);
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
});
}


function get_servicecodes_data(call_back){
         $.ajax({
             type: "GET",
             url: "/rudhospbillitems/"+String(orgid)+"/",
             contentType: "application/json",
             dataType: "json",
             success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
                    call_back(data,status);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
        });
}
function update_servicecode(data,call_back){
         $.ajax ({
 type: "PUT",
 url: "/rudhospbillitems/"+data.id+"/",
 contentType: "application/json",
 data:JSON.stringify(data),
 dataType: "json",
 success: function (data, status) {
//        alert("Data: " + data + "\nStatus: " + status);
        call_back(data,status);
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
});
}
function delete_servicecode(id, call_back) {
     $.ajax ({
        url: '/rudhospbillitems/' + id +"/",
        type: 'DELETE',
        success: function(data,status) {
            call_back(data,status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log( XMLHttpRequest.responseText);
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
    });
}


function save_servicetax(data, call_back){

    $.ajax({
 type: "POST",
 url: "/createhospservicetax/",
 data: JSON.stringify(data),
 contentType: "application/json",
 dataType: "json",
 success: function (data, status) {
//        alert("Data: " + data + "\nStatus: " + status);
        call_back(data,status);
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log( XMLHttpRequest.responseText);
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
});
}


function get_servicetax_data(call_back){
         $.ajax({
             type: "GET",
             url: "/rudhospservicetax/"+String(orgid)+"/",
             contentType: "application/json",
             dataType: "json",
             success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
                    call_back(data,status);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
        });
}
function update_servicetax(data,call_back){
         $.ajax ({
 type: "PUT",
 url: "/rudhospservicetax/"+data.id+"/",
 contentType: "application/json",
 data:JSON.stringify(data),
 dataType: "json",
 success: function (data, status) {
//        alert("Data: " + data + "\nStatus: " + status);
        call_back(data,status);
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
});
}
function delete_servicetax(id, call_back) {
     $.ajax ({
        url: '/rudhospservicetax/' + id +"/",
        type: 'DELETE',
        success: function(data,status) {
            call_back(data,status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log( XMLHttpRequest.responseText);
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
    });
}


function save_newitemtobilll(data, call_back){

    $.ajax({
 type: "POST",
 url: "/creatpatienteorderiteam/",
 data: JSON.stringify(data),
 contentType: "application/json",
 dataType: "json",
 success: function (data, status) {



//        alert("Data: " + data + "\nStatus: " + status);
        call_back(data,status);
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log( XMLHttpRequest.responseText);
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
});
}



function get_newitemtobilll_data(call_back){
         $.ajax({
             type: "GET",
             url: "/billsreport/items/"+String(orderid_id)+"/",
             contentType: "application/json",
             dataType: "json",
             success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
                    call_back(data,status);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
        });
}



function get_billtaxtable_data(call_back){
         $.ajax({
             type: "GET",
             url: "/billsreport/tax/"+String(orderid_id)+"/",
             contentType: "application/json",
             dataType: "json",
             success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
                    call_back(data,status);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
        });
}


function save_newpaymentobilll(data, call_back){

    $.ajax({
 type: "POST",
 url: "/billsreport/payment/"+String(orderid_id)+"/",
 data: JSON.stringify(data),
 contentType: "application/json",
 dataType: "json",
 success: function (data, status) {



//        alert("Data: " + data + "\nStatus: " + status);
        call_back(data,status);
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log( XMLHttpRequest.responseText);
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
});
}


function get_paymentobilll_data(call_back){
         $.ajax({
             type: "GET",
             url: "/billsreport/payment/"+String(orderid_id)+"/",
             contentType: "application/json",
             dataType: "json",
             success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
                    call_back(data,status);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
        });
}


function save_newtaxtobilll(data, call_back){

    $.ajax({
 type: "POST",
 url: "/patientorderservicetax/"+String(orderid_id)+"/",
 data: JSON.stringify(data),
 contentType: "application/json",
 dataType: "json",
 success: function (data, status) {



//        alert("Data: " + data + "\nStatus: " + status);
        call_back(data,status);
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log( XMLHttpRequest.responseText);
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
});
}


function get_newtaxobilll_data(call_back){
         $.ajax({
             type: "GET",
             url: "/billsreport/payment/"+String(orderid_id)+"/",
             contentType: "application/json",
             dataType: "json",
             success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
                    call_back(data,status);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
        });
}

function update_paymentobilll_data(call_back){
         $.ajax({
             type: "PUT",
             url: "/billsreport/payment/"+String(orderid_id)+"/",
             contentType: "application/json",
             dataType: "json",
             success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
                    call_back(data,status);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
        });
}

function get_hospitalbillreports_data(call_back){
         $.ajax({
             type: "GET",
             url: "/hospbillsreport/",
             contentType: "application/json",
             dataType: "json",
             success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
                    details=data;
                    call_back(data,status);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                //Process error actions
                console.log(XMLHttpRequest.status + ' ' +
                    XMLHttpRequest.statusText);
                return false;
              }
        });
}