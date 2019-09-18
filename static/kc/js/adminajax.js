//save saff
function save_staff(data, call_back) {
    // console.log("save staff")
    $.ajax({
        type: "POST",
        url: "/staff/",
        data: JSON.stringify(data),
        headers: { "X-CSRFToken": $crf_token },
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            // console.log(XMLHttpRequest.responseText);
            // var abc = XMLHttpRequest.responseJSON;
            // console.log(abc);
            var a = JSON.parse(XMLHttpRequest.responseText);
	    for (let errorMessage of Object.values(a.staff)) {
                var err=''
                err += errorMessage;
                 $("#dialogboxDoctor1").show();
                 $("#errorMsgFirstName").html(err);
                 $("#dialogboxDoctor1").delay(4000).fadeOut();
                //nurse
                $("#dialogboxNurse").show();
                $("#errorMsgFname").html(err);
                $("#dialogboxNurse").delay(4000).fadeOut();
                //meddtech
                $("#dialogboxmedTech").show();
                $("#errorMsgFname").html(err);
                $("#dialogboxmedTech").delay(4000).fadeOut();

             }
            console.log('json object of a :', a)
            var b = a.doc;

            return false;
        }
    });
}
//save hr
function save_corp_hr(data, call_back) {
    // console.log("save corphr")
    $.ajax({
        type: "POST",
        url: "/corporatehr/",
        data: JSON.stringify(data),
        headers: { "X-CSRFToken": $crf_token },
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.responseText);
	    a= XMLHttpRequest.responseText
            obj = JSON.parse(a)
            $("#dialogbox").show();
            $("#errorMsg").html(obj["hr"]["email"][0]);
            $("#dialogbox").delay(4000).fadeOut();
            return false;
        }
    });
}
//save distributor
function save_org(data, call_back) {
    // console.log("save orgdata")
    $.ajax({
        type: "POST",
        url: "/distributor/",
        data: JSON.stringify(data),
        headers: { "X-CSRFToken": $crf_token },
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            // console.log(XMLHttpRequest.responseText);
            // var abc = XMLHttpRequest.responseJSON;
            // console.log(abc);
            var a = JSON.parse(XMLHttpRequest.responseText);
            console.log('json object of a :', a)
            // var b = a.doc;

            return false;
        }
    });
}
//save branch
function save_branch(data, call_back) {
    // console.log("save orgdata")
    $.ajax({
        type: "POST",
        url: "/branch/",
        data: JSON.stringify(data),
        headers: { "X-CSRFToken": $crf_token },
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
                //  alert("Data: " + data + "\nStatus: " + status);
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            // console.log(XMLHttpRequest.responseText);
            var abc = XMLHttpRequest.responseJSON;
            console.log(abc);
            var a = JSON.parse(XMLHttpRequest.responseText);
            console.log('json object of a :', a)
            var b = a.doc;

            return false;
        }
    });
}
//save corporate
function save_corp(data, call_back) {
    // console.log("save orgdata")
    $.ajax({
        type: "POST",
        url: "/corporate/",
        data: JSON.stringify(data),
        headers: { "X-CSRFToken": $crf_token },
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            // console.log(XMLHttpRequest.responseText);
            var abc = XMLHttpRequest.responseJSON;
            console.log(abc);
            var a = JSON.parse(XMLHttpRequest.responseText);
            console.log('json object of a :', a)
            var b = a.doc;

            return false;
        }
    });
}

function get_branches_data(call_back) {
    // console.log(" ### get_branches_data ###");
    $.ajax({
        type: "GET",
        url: "/branches/",
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
            // console.log(data, "b data");
            var branch_code = '<option value="" selected disabled >Select Branch</option>';

            if (data.length >= 0) {
                for (var i = 0; i < data.length; i++) {
                    var alr = data[i]

                    branch_code += '<option val=' + alr.branch_code + '>' + alr.branch_code + '</option>';

                }
                $("#branchcode").html(branch_code);
            }
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +XMLHttpRequest.statusText);

            return false;
        }
    });
}

function get_doctor_data(call_back) {
    // console.log(" ### get_doctors_data ###");
    $.ajax({
        type: "GET",
        url: "/doctors/",
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +
                XMLHttpRequest.statusText);

            return false;
        }
    });
}
function get_nurse_data(call_back) {
    // console.log(" ### get_nurse_data ###");
    $.ajax({
        type: "GET",
        url: "/nurses/",
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +
                XMLHttpRequest.statusText);

            return false;
        }
    });
}
function get_medTech_data(call_back) {
    // console.log(" ### get_medtech_data ###");
    $.ajax({
        type: "GET",
        url: "/medtechs/",
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
            // console.log("get med tech data::", data)
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +
                XMLHttpRequest.statusText);

            return false;
        }
    });
}
function getpatients(urlpath,call_back) {
    // console.log(" ### get_patients_data ###");
    $.ajax({
        type: "GET",
        url:urlpath,
        // url: "/patientcops/",
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
            // console.log("get med tech data::", data)
            //        alert("Data: " + data + "\nStatus: " + status);
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +
                XMLHttpRequest.statusText);

            return false;
        }
    });
}

function update_staff(data, call_back) {
    $.ajax({
        type: "PATCH",

        url: "/staff/" + data.staff + "/",
        headers: { "X-CSRFToken": $crf_token },
        contentType: "application/json",
        data: JSON.stringify(data),
        dataType: "json",
        success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +
                XMLHttpRequest.statusText);
            return false;
        }
    });
}
function delete_staff(id, call_back) {
    jQuery.ajax({
        url: '/staff/' + id + "/",
	headers: { "X-CSRFToken": $crf_token },
        type: 'DELETE',
        success: function (data, status) {
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +
                XMLHttpRequest.statusText);
            return false;
        }
    });
}

function get_branch_data(call_back){
    // console.log(" ### get_branches_data ###");
    $.ajax({
        type: "GET",
        url: "/branches/",
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
            // console.log(data, "b data");
            var branch_code = '<option value="" selected disabled >Select Branch</option>';
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +
                XMLHttpRequest.statusText);

            return false;
        }
    });

}

function get_corporate_data(call_back){
    // console.log(" ### get_branches_data ###");
    $.ajax({
        type: "GET",
        url: "/corporates/",
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
            // console.log(data, "b data");
            var branch_code = '<option value="" selected disabled >Select Branch</option>';
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +
                XMLHttpRequest.statusText);

            return false;
        }
    });

}
function get_corphr_data(call_back) {
    // console.log(" ### get_doctors_data ###");
    $.ajax({
        type: "GET",
        url: "/corporatehrs/",
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +
                XMLHttpRequest.statusText);

            return false;
        }
    });
}

function get_organization_data(call_back){
    // console.log(" ### get_branches_data ###");
    $.ajax({
        type: "GET",
        url: "/distributors/",
        contentType: "application/json",
        dataType: "json",
        success: function (data, status) {

            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +
                XMLHttpRequest.statusText);

            return false;
        }
    });

}

function update_corphr(data, call_back) {
    $.ajax({
        type: "PATCH",

        url: "/corporatehr/" + data.hr.id + "/",
        headers: { "X-CSRFToken": $crf_token },
        contentType: "application/json",
        data: JSON.stringify(data),
        dataType: "json",
        success: function (data, status) {
            //        alert("Data: " + data + "\nStatus: " + status);
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +
                XMLHttpRequest.statusText);
            return false;
        }
    });
}

function delete_corphr(id, call_back) {
    jQuery.ajax({
        url: '/corporatehr/' + id + "/",
	headers: { "X-CSRFToken": $crf_token },
        type: 'DELETE',
        success: function (data, status) {
            call_back(data, status);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            //Process error actions
            // console.log(XMLHttpRequest.responseText);
            console.log(XMLHttpRequest.status + ' ' +
                XMLHttpRequest.statusText);
            return false;
        }
    });
}
