
$(function () {
    // console.log("deeded");
    var load_branch_code = function () {
        get_branches_data(function (data, status) {
            // console.log(data)
        });
    }
    load_branch_code();
});

/*doctor end*/
$(function () {
    var load_doctor = function () {
        get_doctor_data(function (data, status) {
            var doctor_view = ""
            // console.log("get doctor data", data)
            if (data.length >= 0) {
                for (var i = 0; i < data.length; i++) {
                    var alr = data[i]
                    doctor_view += '<tr >';
                    doctor_view += '<td><span>' + alr.pro.first_name + ' ' + '</span><span>' + alr.pro.middle_name + ' ' + '</span><span>' + alr.pro.last_name + '</span></td>';
                    doctor_view += '<td><span>' + alr.branch_code + '</span></td>';
                    doctor_view += '<td><span>' + alr.Licence_number + '</span></td>';
                    doctor_view += '<td><span>' + alr.pro.Qualification + '</span></td>';
                    doctor_view += '<td><span>' + alr.speciality + '</span></td>';

                    doctor_view += '<td><span>' + alr.Experience + '</span></td>';
                    doctor_view += '<td style="display: none;" ><span>' + alr.pro.gender + '</span></td>';
                    var a = alr.pro.phone.split(" ");
                    var phon = a[1]
                    // console.log("phone number " + phon)
                    doctor_view += '<td style="display: none;" ><span>' + phon + '</span></td>';
                    doctor_view += '<td style="display: none;"><span>' + alr.staff.email + '</span></td>';
                    // console.log("Experience: ", alr.Experience)
                    var exp = alr.Experience.split(" ")
                    var expyear = exp[0]
                    var expmon = exp[2]
                    // console.log("year: " + expyear + " month: " + expmon)
                    doctor_view += '<td style="display: none;"><span>' + expyear + '</span><span>' + expmon + '</td>';
                    // doctor_view += '<td style="display: none;"><span>' + alr.branch_code + '</span></td>';
                    doctor_view += '<td ><a style="color: #64c1b1; " href="/profile/' + alr.staff.id + '/"class="fa fa-user-circle fa-lg" ></a></td>';
                    if(suser=="superadmin"){
                        doctor_view += '<td style=" display:none"><a style="color: #64c1b1;" href="javascript:void(0)" data-id="' + alr.staff.id + '" class="doctoredit fa fa-pencil-square-o "></a> </td>';
                        doctor_view += '<td style=" display:none"><a style="color: #64c1b1;"  href="javascript:void(0)" data-id="' + alr.staff.id + '" class="doctordelete fa fa-trash-o"></a></td>';
                    }
                    else{
                        doctor_view += '<td ><a style="color: #64c1b1;" href="javascript:void(0)" data-id="' + alr.staff.id + '" class="doctoredit fa fa-pencil-square-o "></a> </td>';
                        doctor_view += '<td><a style="color: #64c1b1;"  href="javascript:void(0)" data-id="' + alr.staff.id + '" class="doctordelete fa fa-trash-o"></a></td>';
                    }    
                    doctor_view += '</tr>';
                }
                $("#myTable").html(doctor_view);


            }
        });
    }
    var new_dialog = function (type, row, doctor_id) {
        var dlg = $("#doctor-form");
        type = type || 'Create';
        var config = {
            autoOpen: true,
            height: 300,
            width: 786,
            modal: true,
            buttons: {
                "Create": save_doctor_data,
                "Cancel": function () {
                    dlg.dialog("close");
                }
            },
            close: function () {
                dlg.dialog("close");
            }
        };

        if (type === 'Edit') {
            get_doctor_data_for_edit(row);
            delete (config.buttons['Create']);
            config.buttons['Save'] = function () {
                edit_doctor_data(doctor_id)
                row.remove();
            };
            config.buttons['Cancel'] = function () {
                $("#docfname").val("");
                $("#docmname").val("");
                $("#doclname").val("");
                $("#doccontact").val("");
                $("#docgender,#docgendername").val("").show();
                $("#docemaillabel,#docemailinput").val("").show();
                $("#docspeciality").multiselect("clearSelection");
                $("#docspeciality").multiselect('refresh');
                $("#branchcode").val("");
                $("#docqualification").multiselect("clearSelection");
                $("#docqualification").multiselect('refresh');
                // $("#docqualification,#docqualification,#docqualificationvalue,.multiselect,#docqualificationname,#docqualificationnamen").show();
                $("#doclicense,#doclicensename").val("");
                $("#selectYear,#docexperience").val('0');
                $("#branchcode").val("");
                load_doctor();
                dlg.dialog("close");
            };
        }
        dlg.dialog(config);
        function get_doctor_data_for_edit(row) {
            $("#docfname").val($(row.children().find('span').get(0)).text());
            $("#docmname").val($(row.children().find('span').get(1)).text());
            $("#doclname").val($(row.children().find('span').get(2)).text());
            $("#doccontact").val($(row.children().find('span').get(9)).text());
            $("#docgender,#docgendername").hide();
            $("#docemaillabel,#docemailinput").hide();
            $("#branchcode").val($(row.children().find('span').get(3)).text());
           
            // $("#docqualification").val($(row.children().find('span').get(5))).text();

            //qualification
            $("#docqualification").multiselect({
                selectedText: "# of # selected",
                numberDisplayed: 1,
            });
            var qvalue = $(row.children().find('span').get(5)).text()
            var selectedqOptions = qvalue.split(",");
            var allq=[]
            for(var i in selectedqOptions) {
                var optionVal = selectedqOptions[i];
                allq.push(optionVal);
            }
             $("#docqualification,.multiselect").val(allq).show();
             $("#docqualification").multiselect('refresh');
             //speciality
            $("#docspeciality").multiselect({
                selectedText: "# of # selected",
                numberDisplayed: 1,
             });
             var hidValue = $(row.children().find('span').get(6)).text()
            var selectedOptions = hidValue.split(",");
            var all=[]
            for(var i in selectedOptions) {
                var optionVal = selectedOptions[i];
                all.push(optionVal);
            }
            $("#docspeciality,.multiselect").val(all).show();
            $("#docspeciality").multiselect('refresh');

            var experience = $(row.children().find('span').get(10)).text();
            var splitExperience = experience.split(" ");
            var year = splitExperience[0];
            var month = splitExperience[2];
            $("#selectYear").val($(row.children().find('span').get(11)).text());
            $("#docexperience").val($(row.children().find('span').get(12)).text());
            $("#doclicense").val($(row.children().find('span').get(4)).text());
        }
        function edit_doctor_data(id) {
            var fname = $("#docfname").val();
            var mname = $("#docmname").val();
            var lname = $("#doclname").val();
            var countryCode = $("#docCountryCode").val();
            var contactNo = $("#doccontact").val();
            var contact = countryCode + ' ' + contactNo;
            var gender = $("#docgender").val();
            var email = $("#docemail").val();
            var speciality = $("#docspeciality").val();
            if (speciality !== null) {
                var speciality = speciality.join();
            }
            else {
                var speciality = "";
            }
            var docQualification = $("#docqualification").val();
            if (docQualification !== null) {
                var docQualification = docQualification.join();
            }
            else {
                var docQualification = "";
            }
            var branchCode = $("#branchcode").val();
            var experiencemonth = $("#docexperience").val();
            var experienceyear = $("#selectYear").val();
            var experience = experienceyear + ' years ' + experiencemonth + ' months'
            var license = $("#doclicense").val();
            
            if (fname == '') {
                $("#dialogboxDoctor1").show();
                $("#errorMsgFirstName").html('First name is mandatory');
                $("#dialogboxDoctor1").delay(4000).fadeOut();
            }
            else if (lname == '') {
                $("#dialogboxDoctor9").show();
                $("#errorMsgLastName").html('Last name is mandatory');
                $("#dialogboxDoctor9").delay(4000).fadeOut();
            }

            else if ( contactNo.length <= 9) {
                if (contactNo == '') {
                    
                $("#dialogboxDoctor2").show();
                $("#errorMsgContact").html('Contact number is mandatory');
                $("#dialogboxDoctor2").delay(4000).fadeOut();
                }
                else if(contactNo.length < 10){
                $("#dialogboxDoctor2").show();
                $("#errorMsgContact").html('Contact number should be 10 digits');
                $("#dialogboxDoctor2").delay(4000).fadeOut();
                }
            }
            
            else if (branchCode == null) {
                $("#dialogboxDoctor3").show();
                $("#errorMsgUsername").html('Branch code is mandatory');
                $("#dialogboxDoctor3").delay(4000).fadeOut();
            }
            else if (speciality == '') {
                $("#dialogboxDoctor5").show();
                $("#errorMsgSpeciality").html('Speciality is mandatory');
                $("#dialogboxDoctor5").delay(4000).fadeOut();
            }
            else if (docQualification == '') {
                $("#dialogboxDoctor5").show();
                $("#errorMsgSpeciality").html('Qualification is mandatory');
                $("#dialogboxDoctor5").delay(4000).fadeOut();
            }
            else if (experience == '0 years 0 months') {
                $("#dialogboxDoctor6").show();
                $("#errorMsgExperience").html('Experience is mandatory');
                $("#dialogboxDoctor6").delay(4000).fadeOut();
            }
            else if (license == '') {
                $("#dialogboxDoctor7").show();
                $("#errorMsgLicenceNumber").html('Licence number is mandatory');
                $("#dialogboxDoctor7").delay(4000).fadeOut();
            }
           
            else {

                var doctor_data = {
                    "staff": id,
                    "pro": {
                        // "gender": gender,
                        "first_name": fname,
                        "middle_name": mname,
                        "last_name": lname,
                        "Qualification": docQualification,
                        "user_type": 3,
                        "phone": contact
                    },
                    "branch_code": branchCode,
                    "speciality": speciality,
                    "Experience": experience,
                    "Licence_number": license
                }
                // console.log("", doctor_data)
                update_staff(doctor_data, function (data, status) {
                    if (status == "success") {
                        $("#docfname").val("");
                        $("#docmname").val("");
                        $("#doclname").val("");
                        $("#doccontact").val("");
                        $("#docgender,#docgendername").val("").show();
                        $("#docemaillabel,#docemailinput").val("").show();
                        // $("#docspeciality,#docspecialityname").val("");
                        $("#docqualification,#docspeciality").multiselect("clearSelection");
                        $("#docqualification,#docspeciality").multiselect('refresh');
                        $("#doclicense,#doclicensename").val("");
                        $("#selectYear,#docexperience").val('0');
                        $("#branchcode").val("");
                        load_doctor();
                        dlg.dialog("close");
                    }
                });
            }
        }

        function save_doctor_data() {

            var fname = $("#docfname").val();
            var mname = $("#docmname").val();
            var lname = $("#doclname").val();
            var countryCode = $("#docCountryCode").val();
            var contactNo = $("#doccontact").val();
            var contact = countryCode + ' ' + contactNo;
            // console.log(contact)
            var gender = $("#docgender").val();
            var email = $("#docemail").val();
            var speciality = $("#docspeciality").val();
            if (speciality !== null) {
                var speciality = speciality.join();
            }
            else {
                var speciality = "";
            }
            var docQualification = $("#docqualification").val();
            if (docQualification !== null) {
                var qualification = docQualification.join();
            }
            else {
                var qualification = "";
            }
            var experiencemonth = $("#docexperience").val();
            var experienceyear = $("#selectYear").val();
            var experience = experienceyear + ' years ' + experiencemonth + ' months'
            var branchCode = $("#branchcode").val();
            var license = $("#doclicense").val();
            
            var atposition=email.indexOf("@");  
            var dotposition=email.lastIndexOf(".");  
            
            if (fname == '') {
                $("#dialogboxDoctor1").show();
                $("#errorMsgFirstName").html('First name is mandatory');
                $("#dialogboxDoctor1").delay(4000).fadeOut();
            }
            else if (lname == '') {
                $("#dialogboxDoctor9").show();
                $("#errorMsgLastName").html('Last name is mandatory');
                $("#dialogboxDoctor9").delay(4000).fadeOut();
            }

            else if ( contactNo.length <= 9) {
                if (contactNo == '') {
                    
                $("#dialogboxDoctor2").show();
                $("#errorMsgContact").html('Contact number is mandatory');
                $("#dialogboxDoctor2").delay(4000).fadeOut();
                }
                else if(contactNo.length < 10){
                $("#dialogboxDoctor2").show();
                $("#errorMsgContact").html('Contact number should be 10 digits');
                $("#dialogboxDoctor2").delay(4000).fadeOut();
                }
            }
            else if(gender==null){
                $("#dialogboxDoctor2").show();
                $("#errorMsgContact").html('Gender is mandatory');
                $("#dialogboxDoctor2").delay(4000).fadeOut();
            }
            else if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length) {
                if (email == ''){
                    $("#dialogboxDoctor8").show();
                    $("#errorMsgemail").html('Email address is mandatory');
                    $("#dialogboxDoctor8").delay(4000).fadeOut();
                }
                else {
                    $("#dialogboxDoctor8").show(); 
                    $("#errorMsgemail").html("Please enter a valid e-mail address");
                    $("#dialogboxDoctor8").delay(4000).fadeOut();  
                } 
            }
            else if (branchCode == null) {
                $("#dialogboxDoctor3").show();
                $("#errorMsgUsername").html('Branch code is mandatory');
                $("#dialogboxDoctor3").delay(4000).fadeOut();
            }
            else if (speciality == '') {
                $("#dialogboxDoctor5").show();
                $("#errorMsgSpeciality").html('Speciality is mandatory');
                $("#dialogboxDoctor5").delay(4000).fadeOut();
            }
            else if (experience == '0 years 0 months') {
                $("#dialogboxDoctor6").show();
                $("#errorMsgExperience").html('Experience is mandatory');
                $("#dialogboxDoctor6").delay(4000).fadeOut();
            }
            else if (license == '') {
                $("#dialogboxDoctor7").show();
                $("#errorMsgLicenceNumber").html('Licence number is mandatory');
                $("#dialogboxDoctor7").delay(4000).fadeOut();
            }
            else if (qualification == '') {
                $("#dialogboxDoctor4").show();
                $("#errorMsgQualification").html('Qualification is mandatory');
                $("#dialogboxDoctor4").delay(4000).fadeOut();
            }
            // }
            else {

                var doctor_data = {

                    "email": email,
                    "gender": gender,
                    "first_name": fname,
                    "middle_name": mname,
                    "last_name": lname,
                    "Qualification": qualification,
                    "user_type": 3,
                    "phone": contact,
                    "branch_code": branchCode,
                    "speciality": speciality,
                    "Experience": experience,
                    "Licence_number": license
                }

                save_staff(doctor_data, function (data, status) {
                    if (status == "success") {
                        $("#docfname").val("");
                        $("#docmname").val("");
                        $("#doclname").val("");
                        $("#doccontact").val("");
                        $("#docgender,#docgendername").val("").show();
                        $("#docemail,#docemailname").val("");
                        // $("#docspeciality,#docspecialityname").val("");
                        $("#docspeciality").multiselect("clearSelection");
                        $("#docspeciality").multiselect('refresh');
                        // $("#docqualification").val([]);
                        $("#selectYear,#docexperience,#docexperiencenamen,#docexperiencename").val("").show();
                        $("#docqualification").multiselect("clearSelection");
                        $("#docqualification").multiselect('refresh');
                        $("#selectYear,#docexperience").val('0');
                        $("#branchcode").val("");
                        load_doctor();

                        dlg.dialog("close");
                    }
                });
            }
        }
    };


    $(document).on('click', 'a.doctordelete', function () {
        id = $(this).data('id');
        //        alert("delete ::"+id);
        delete_staff(id, function (data, status) {
            load_doctor();
        });
        return false;
    });
    $(document).on('click', 'td a.doctoredit', function () {
        new_dialog('Edit', $(this).parents('tr'), $(this).data('id'));
        return false;
    });
    $(".doctor-adduser").button().click(new_dialog);

    load_doctor();

});

// /*Nurse*/


$(function () {
    var load_nurse = function () {
        get_nurse_data(function (data, status) {
            // console.log("********");
            var nurse_view = ""
            // console.log(data);

            // console.log(data.length);

            if (data.length >= 0) {

                for (var i = 0; i < data.length; i++) {
                    var alr = data[i]
                    nurse_view += '<tr >';
                    nurse_view += '<td ><span>' + alr.pro.first_name + " " + '</span><span>' + alr.pro.middle_name + " " + '</span><span>' + alr.pro.last_name + '</span></td>';
                    nurse_view += '<td ><span>' + alr.branch_code + '</span></td>';
                    nurse_view += '<td><span>' + alr.Licence_number + '</span></td>';
                    nurse_view += '<td><span>' + alr.pro.Qualification + '</span></td>';
                    nurse_view += '<td><span>' + alr.speciality + '</span></td>';
                    nurse_view += '<td style="display: none;" ><span>' + alr.pro.gender + '</span></td>';
                    var a = alr.pro.phone.split(" ");
                    var phon = a[1]
                    nurse_view += '<td style="display: none;" ><span>' + phon + '</span></td>';
                    nurse_view += '<td style="display: none;"><span>' + alr.staff.email + '</span></td>';
                    nurse_view += '<td><span>' + alr.Experience + '</span></td>';
                    var exp = alr.Experience.split(" ")
                    var expyear = exp[0]
                    var expmon = exp[2]
                    nurse_view += '<td style="display: none;"><span>' + expyear + '</span></td>';
                    nurse_view += '<td style="display: none;"><span>' + expmon + '</span></td>';
                    nurse_view += '<td ><a style="color: #64c1b1; " href="/profile/' + alr.staff.id + '/"class="fa fa-user-circle fa-lg" ></a></td>';
                    if(suser=="superadmin"){
                        nurse_view += '<td style="display:none"><a style="color: #64c1b1; " href="javascript:void(0)" data-id="' + alr.staff.id + '" class="nurseedit fa fa-pencil-square-o "></a> </td>';
                        nurse_view += '<td style="display:none"><a style="color: #64c1b1; ;"  href="javascript:void(0)" data-id="' + alr.staff.id + '" class="nursedelete fa fa-trash-o"></a></td>';
                    }
                    else{
                        nurse_view += '<td><a style="color: #64c1b1; " href="javascript:void(0)" data-id="' + alr.staff.id + '" class="nurseedit fa fa-pencil-square-o "></a> </td>';
                        nurse_view += '<td><a style="color: #64c1b1; ;"  href="javascript:void(0)" data-id="' + alr.staff.id + '" class="nursedelete fa fa-trash-o"></a></td>';
                    }
                    nurse_view += '</tr>';
                }
                $("#NursesTable").html(nurse_view)
            }
        });
    }
    var new_dialog = function (type, row, nurse_id) {
        var dlg = $("#nurse-form");
        type = type || 'Create';
        var config = {
            autoOpen: true,
            height: 300,
            width: 786,
            modal: true,
            buttons: {
                "Create": save_nurse_data,
                "Cancel": function () {
                    $("#nursefname").val("");
                        $("#nursemname").val("");
                        $("#nurselname").val("");
                        $("#nursecontact").val("");
                        $("#nursegender,#nursegender").val("").show();
                        $("#nurseemail,#nurseemailname").val("").show();
                        $("#nursespeciality,#nursespecialityname").val("").show();
                        $('#nursequalification').multiselect('clearSelection');
                        $("#nursequalification").multiselect('refresh');
                        $("#nurseexperience,#selectYear,#nurseexperiencenamen,#nurseexperiencename").val("0").show();
                        $("#nurselicense,#nurselicensename").val(null);
                        load_nurse();
                    dlg.dialog("close");
                }
            },
            close: function () {
                dlg.dialog("close");
            }
        };
        if (type === 'Edit') {

            get_nurse_data_for_edit(row);
            delete (config.buttons['Create']);

            config.buttons['Save'] = function () {
                edit_nurse_data(nurse_id)
                row.remove();
            };
            config.buttons['Cancel'] = function () {

                dlg.dialog("close");
                $("#nursefname").val("");
                $("#nursemname").val("");
                $("#nurselname").val("");
                $("#nursecontact").val("");
                $("#branchcode").val("");
                $("#nursegender,#nursegendername").val("").show();
                $("#nurseemailname,#nurseemailnamei").val("").show();
                $("#nursespeciality,#nursespecialityname").val("").show();
                $("#selectYear, #nurseexperience,#nursequalificationnamen,#nursequalificationname").val("").show();
                $("#selectYear,#nurseexperience").val("0").show();
                $("#nursequalification,#nursespeciality").val("").show();
                $("#nurselicense,#nurselicensename").val("").show();
            };
        }
        dlg.dialog(config);
        function get_nurse_data_for_edit(row) {
            $("#nursefname").val($(row.children().find('span').get(0)).text());
            $("#nursemname").val($(row.children().find('span').get(1)).text());
            $("#nurselname").val($(row.children().find('span').get(2)).text());
            $("#nursecontact").val($(row.children().find('span').get(8)).text());
            $("#branchcode").val($(row.children().find('span').get(3)).text());
            $("#nursegender,#nursegendername").hide();
            $("#nurseemailname,#nurseemailnamei").hide();
            $("#nursequalification").multiselect({
                selectedText: "# of # selected",
                numberDisplayed: 1,
            });
            var qvalue = $(row.children().find('span').get(5)).text()
            var selectedqOptions = qvalue.split(",");
            var allq=[]
            for(var i in selectedqOptions) {
                var optionVal = selectedqOptions[i];
                allq.push(optionVal);
            }
             $("#nursequalification,.multiselect").val(allq).show();
             $("#nursequalification").multiselect('refresh');
            var experience = $(row.children().find('span').get(9)).text();
            var splitExperience = experience.split(" ");
            var year = splitExperience[0];
            var month = splitExperience[2];
            $("#selectYear").val($(row.children().find('span').get(11)).text());
            $("#nurseexperience").val($(row.children().find('span').get(12)).text());

            $("#nursespeciality").multiselect({
                selectedText: "# of # selected",
                numberDisplayed: 1,
             });
             var hidsValue = $(row.children().find('span').get(6)).text();
            var selectedOptions = hidsValue.split(",");
            var alls=[]
            for(var i in selectedOptions) {
                var optionVal = selectedOptions[i];
                alls.push(optionVal);
            }
            $("#nursespeciality,.multiselect").val(alls).show();
            $("#nursespeciality").multiselect('refresh');

            $("#nurselicense").val($(row.children().find('span').get(4)).text());

        }
        function edit_nurse_data(id) {
            var fname = $("#nursefname").val();
            var mname = $("#nursemname").val();
            var lname = $("#nurselname").val();
            var countryCode = $("#countryCode").val();
            var contactNo = $("#nursecontact").val();
            var contact = countryCode + ' ' + contactNo;
            var gender = $("#nursegender").val();
            var email = $("#nurseemail").val();

            var speciality = $("#nursespeciality").val();
            if (speciality !== null) {
                var speciality = speciality.join();
            }
            else {
                var speciality = "";
            }
            var nursequalification = $("#nursequalification").val();
            if (nursequalification !== null) {
                var nursequalification = nursequalification.join();
            }
            else {
                var nursequalification = "";
            }
            var experiencemonth = $("#nurseexperience").val();
            var experienceyear = $("#selectYear").val();
            var experience = experienceyear + ' years ' + experiencemonth + ' months'
            // var experience = $("#nurseexperience").val();
            var branchCode = $("#branchcode").val();
            var license = $("#nurselicense").val();

            if (fname == '') {
                $("#dialogboxNurse").show();
                $("#errorMsgFname").html('First name is mandatory');
                $("#dialogboxNurse").delay(4000).fadeOut();
            }
            else if (lname == '') {
                $("#dialogboxNurse8").show();
                $("#errorMsglname").html('Last name is mandatory');
                $("#dialogboxNurse8").delay(4000).fadeOut();
            }
            else if ( contactNo.length <= 9) {
                if (contactNo == '') {
                    
                    $("#dialogboxNurse1").show();
                    $("#errorMsgContact").html('Contact number is mandatory');
                    $("#dialogboxNurse1").delay(4000).fadeOut();
                }
                else if(contactNo.length < 10){
                    $("#dialogboxNurse1").show();
                    $("#errorMsgContact").html('Contact number should be 10 digits');
                    $("#dialogboxNurse1").delay(4000).fadeOut();
                
                }
            }
            else if (branchCode == null) {
                $("#dialogboxNurse3").show();
                $("#errorMsgSpeciality").html('Branch code is mandatory');
                $("#dialogboxNurse3").delay(4000).fadeOut();
            }
            else if (speciality == '') {
                $("#dialogboxNurse3").show();
                $("#errorMsgSpeciality").html('Speciality is mandatory');
                $("#dialogboxNurse3").delay(4000).fadeOut();
            }
            else if (nursequalification == '') {
                $("#dialogboxNurse3").show();
                $("#errorMsgSpeciality").html('Qualification is mandatory');
                $("#dialogboxNurse3").delay(4000).fadeOut();
            }
            
            else if (license == '') {
                $("#dialogboxNurse5").show();
                $("#errorMsgLicense").html('License number is mandatory');
                $("#dialogboxNurse5").delay(4000).fadeOut();
            }
            else if (experience == '0 years 0 months') {
                $("#dialogboxNurse4").show();
                $("#errorMsgExperience").html('Experience is mandatory');
                $("#dialogboxNurse4").delay(4000).fadeOut();
            }
            

            // }
            else {
            var nurse_data = {

                "staff": id,
                "pro": {

                    // "gender": gender,
                    "first_name": fname,
                    "middle_name": mname,
                    "last_name": lname,
                    "Qualification": nursequalification,
                    "user_type": 2,
                    "phone": contact
                },
                "branch_code": branchCode,
                "speciality": speciality,
                "Experience": experience,
                "Licence_number": license
            }

            // console.log(nurse_data)
            update_staff(nurse_data, function (data, status) {
                if (status == "success") {

                    $("#nursefname").val("");
                    $("#nursemname").val("");
                    $("#nurselname").val("");
                    $("#nursecontact").val("");
                    $("#branchcode").val("");
                    $("#nursegender,#nursegendername").val("").show();
                    $("#nurseemailname,#nurseemailnamei").val("").show();
                    $('#nursequalification,#nursespeciality').multiselect('clearSelection');
                    $("#nursequalification,#nursespeciality").multiselect('refresh');
                    $("#selectYear, #nurseexperience").val("0");
                    $("#nurselicense").val("");
                    load_nurse();
                    dlg.dialog("close");
                }
            });
        }
    }
        function save_nurse_data() {
            var fname = $("#nursefname").val();
            var mname = $("#nursemname").val();
            var lname = $("#nurselname").val();

            var countryCode = $("#countryCode").val();

            var contactNo = $("#nursecontact").val();
            var contact = countryCode + ' ' + contactNo;
            var gender = $("#nursegender").val();
            var email = $("#nurseemail").val();
            var speciality = $("#nursespeciality").val();
            if (speciality !== null) {
                var speciality = speciality.join();
            }
            else {
                var speciality = "";
            }
           
            var nursequalification = $("#nursequalification").val();
            if (nursequalification !== null) {
                nursequalification = nursequalification.join();
            }
            else {
                nursequalification = "";
            }
            var experiencemonth = $("#nurseexperience").val(); 
            var experienceyear = $("#selectYear").val();
            var experience = experienceyear + ' years ' + experiencemonth + ' months'
            var branchCode = $("#branchcode").val();
            var license = $("#nurselicense").val();

            var atposition=email.indexOf("@");  
            var dotposition=email.lastIndexOf(".");  

            if (fname == '') {
                $("#dialogboxNurse").show();
                $("#errorMsgFname").html('First name is mandatory');
                $("#dialogboxNurse").delay(4000).fadeOut();
            }
            else if (lname == '') {
                $("#dialogboxNurse8").show();
                $("#errorMsglname").html('Last name is mandatory');
                $("#dialogboxNurse8").delay(4000).fadeOut();
            }
            else if ( contactNo.length <= 9) {
                if (contactNo == '') {
                    
                    $("#dialogboxNurse1").show();
                    $("#errorMsgContact").html('Contact number is mandatory');
                    $("#dialogboxNurse1").delay(4000).fadeOut();
                }
                else if(contactNo.length < 10){
                    $("#dialogboxNurse1").show();
                    $("#errorMsgContact").html('Contact number should be 10 digits');
                    $("#dialogboxNurse1").delay(4000).fadeOut();
                
                }
            }
            else if (gender == null) {
                $("#dialogboxNurse3").show();
                $("#errorMsgSpeciality").html('Gender is mandatory');
                $("#dialogboxNurse3").delay(4000).fadeOut();
            }
           
            else if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length) {
                if (email == ''){
                    $("#dialogboxNurse7").show();
                    $("#errorMsgemail").html('Email address is mandatory');
                    $("#dialogboxNurse7").delay(4000).fadeOut();
                }
                else {
                    $("#dialogboxNurse7").show();
                    $("#errorMsgemail").html('Please enter a valid email address');
                    $("#dialogboxNurse7").delay(4000).fadeOut();
                } 
            } 
            else if (branchCode == null) {
                $("#dialogboxNurse3").show();
                $("#errorMsgSpeciality").html('Branch code is mandatory');
                $("#dialogboxNurse3").delay(4000).fadeOut();
            }
            else if (speciality == '') {
                $("#dialogboxNurse3").show();
                $("#errorMsgSpeciality").html('Speciality is mandatory');
                $("#dialogboxNurse3").delay(4000).fadeOut();
            }
            else if (nursequalification == '') {
                $("#dialogboxNurse3").show();
                $("#errorMsgSpeciality").html('Qualification is mandatory');
                $("#dialogboxNurse3").delay(4000).fadeOut();
            }
            else if (license == '') {
                $("#dialogboxNurse5").show();
                $("#errorMsgLicense").html('License number is mandatory');
                $("#dialogboxNurse5").delay(4000).fadeOut();
            }
           
            else if (experience == '0 years 0 months') {
                $("#dialogboxNurse4").show();
                $("#errorMsgExperience").html('Experience is mandatory');
                $("#dialogboxNurse4").delay(4000).fadeOut();
            }
            

            // }
            else {


                var nurse_data = {

                    "email": email,
                    "gender": gender,
                    "first_name": fname,
                    "middle_name": mname,
                    "last_name": lname,
                    "Qualification": nursequalification,
                    "user_type": 2,
                    "phone": contact,
                    "branch_code": branchCode,
                    "speciality": speciality,
                    "Experience": experience,
                    "Licence_number": license
                }

                save_staff(nurse_data, function (data, status) {
                    if (status == "success") {
                        $("#nursefname").val("");
                        $("#nursemname").val("");
                        $("#nurselname").val("");
                        $("#nursecontact").val("");
                        $("#nursegender,#nursegender").val("").show();
                        $("#nurseemail,#nurseemailname").val("").show();
                        $("#nursespeciality,#nursespecialityname").val("").show();
                        $('#nursequalification,#nursespeciality').multiselect('clearSelection');
                        $("#nursequalification,#nursespeciality").multiselect('refresh');
                        $("#nurseexperience,#selectYear,#nurseexperiencenamen,#nurseexperiencename").val("0").show();
                        $("#nurselicense,#nurselicensename").val(null);
                        $("#branchcode").val("");
                        load_nurse();
                        dlg.dialog("close");
                    }
                });
            }
        }
    };
    $(document).on('click', 'a.nursedelete', function () {
        id = $(this).data('id');
        //        alert("delete ::"+id);
        delete_staff(id, function (data, status) {
            load_nurse();
        });
        return false;
    });
    $(document).on('click', 'td a.nurseedit', function () {
        new_dialog('Edit', $(this).parents('tr'), $(this).data('id'));
        return false;
    });
    $(".nurse-adduser").button().click(new_dialog);

    load_nurse();

});

/* MedTech people */

$(function () {
    var load_medTech = function () {
        get_medTech_data(function (data, status) {
            // console.log("medd tech people data", data);
            var medTech_view = ""
            if (data.length >= 0) {

                for (var i = 0; i < data.length; i++) {
                    var alr = data[i]
                    medTech_view += '<tr >';
                    medTech_view += '<td ><span>' + alr.pro.first_name + " " + '</span><span>' + alr.pro.middle_name + " " + '</span><span>' + alr.pro.last_name + '</span></td>';
                    medTech_view += '<td ><span>' + alr.branch_code + '</span></td>';
                    medTech_view += '<td><span>' + alr.Licence_number + '</span></td>';
                    medTech_view += '<td><span>' + alr.pro.Qualification + '</span></td>';
                    medTech_view += '<td><span>' + alr.speciality + '</span></td>';
                    medTech_view += '<td style="display: none;" ><span>' + alr.pro.gender + '</span></td>';
                    var a = alr.pro.phone.split(" ");
                    var phon = a[1]
                    medTech_view += '<td style="display: none;" ><span>' + phon + '</span></td>';
                    // nurse_view += '<td style="display: none;" ><span>' + alr.nurse_user.username + '</span></td>';
                    medTech_view += '<td style="display: none;"><span>' + alr.staff.email + '</span></td>';
                    medTech_view += '<td><span>' + alr.Experience + '</span></td>';
                    // console.log("Experience: ", alr.Experience)
                    var exp = alr.Experience.split(" ")
                    var expyear = exp[0]
                    var expmon = exp[2]
                    medTech_view += '<td style="display: none;"><span>' + expyear + '</span></td>';
                    medTech_view += '<td style="display: none;"><span>' + expmon + '</span></td>';
                    medTech_view += '<td ><a style="color: #64c1b1; " href="/profile/' + alr.staff.id + '/"class="fa fa-user-circle fa-lg" ></a></td>';
                    if(suser=="superadmin"){ 
                        medTech_view += '<td style=" display:none"><a style="color: #64c1b1; " href="javascript:void(0)" data-id="' + alr.staff.id + '" class="medTechedit fa fa-pencil-square-o "></a> </td>';
                        medTech_view += '<td style=" display:none"><a style="color: #64c1b1; ;"  href="javascript:void(0)" data-id="' + alr.staff.id + '" class="medTechdelete fa fa-trash-o"></a></td>';
                    }
                    else{
                        medTech_view += '<td><a style="color: #64c1b1; " href="javascript:void(0)" data-id="' + alr.staff.id + '" class="medTechedit fa fa-pencil-square-o "></a> </td>';
                        medTech_view += '<td><a style="color: #64c1b1; ;"  href="javascript:void(0)" data-id="' + alr.staff.id + '" class="medTechdelete fa fa-trash-o"></a></td>';
                    }
                    medTech_view += '</tr>';
                }
                $("#MedTechsTable").html(medTech_view)
            }
        });
    }
    var new_dialog = function (type, row, medTech_id) {
        var dlg = $("#medTech-form");
        type = type || 'Create';
        var config = {
            autoOpen: true,
            height: 300,
            width: 786,
            modal: true,
            buttons: {
                "Create": save_medTech_data,
                "Cancel": function () {
                    $("#medTechfname").val("");
                    $("#medTechmname").val("");
                    $("#medTechlname").val("");
                    $("#medTechcontact").val("");
                    $("#medTechgender,#medTechgender").val("").show();
                    $("#medTechemail,#medTechemailname").val("").show();
                    $("#branchcode").val("").show();
                    $("#medTechqualification,#medTechspeciality").multiselect('clearSelection');
                    $("#medTechqualification,#medTechspeciality").multiselect('refresh');
                    $("#medTechexperience,#selectYear").val('0').show();
                    $("#medTechlicense,#medTechlicensename").val(null);
                    load_medTech();

                    dlg.dialog("close");
                }
            },
            close: function () {
                dlg.dialog("close");
            }
        };
        if (type === 'Edit') {

            get_medTech_data_for_edit(row);
            delete (config.buttons['Create']);

            config.buttons['Save'] = function () {
                edit_medTech_data(medTech_id)
                row.remove();
            };
            config.buttons['Cancel'] = function () {

                dlg.dialog("close");
                $("#medTechfname").val("");
                $("#medTechmname").val("");
                $("#medTechlname").val("");
                $("#medTechcontact").val("");
                $("#branchcode").val("");
                $("#medTechgender,#medTechgendername").val("").show();
                $("#medTechemailname,#medTechemailnamei").show();
                $("#medTechqualification,#medTechspeciality").multiselect('clearSelection');
                $("#medTechqualification,#medTechspeciality").multiselect('refresh');
                $("#selectYear, #medTechexperience").val("0").show();
                $("#medTechlicense,#medTechlicensename").val("").show();
            };
        }
        dlg.dialog(config);
        function get_medTech_data_for_edit(row) {
            $("#medTechfname").val($(row.children().find('span').get(0)).text());
            $("#medTechmname").val($(row.children().find('span').get(1)).text());
            $("#medTechlname").val($(row.children().find('span').get(2)).text());
            $("#branchcode").val($(row.children().find('span').get(3)).text());
            $("#medTechcontact").val($(row.children().find('span').get(8)).text());

            //            $("#nursegender").val($(row.children().find('span').get(3)).text());
            $("#medTechgender,#medTechgendername").hide();

            $("#medTechemailname,#medTechemailnamei").hide();
            $("#medTechqualification").multiselect({
                selectedText: "# of # selected",
                numberDisplayed: 1,
            });
            var quvalue = $(row.children().find('span').get(5)).text();
            
            var selectedquOptions = quvalue.split(",");
            var allq=[]
            for(var i in selectedquOptions) {
                var optionqVal = selectedquOptions[i];
                allq.push(optionqVal);
            }
             $("#medTechqualification,.multiselect").val(allq).show();
             $("#medTechqualification").multiselect('refresh');

            $("#medTechexperiencenamen,#medTechexperiencename").val($(row.children().find('span').get(9)).text());
            var experience = $(row.children().find('span').get(9)).text();
            var splitExperience = experience.split(" ");
            var year = splitExperience[0];
            var month = splitExperience[2];
            $("#selectYear").val($(row.children().find('span').get(11)).text());
            $("#medTechexperience").val($(row.children().find('span').get(12)).text());

            $("#medTechspeciality").multiselect({
                selectedText: "# of # selected",
                numberDisplayed: 1,
            });
            var svalue = $(row.children().find('span').get(6)).text()
            var selectedsOptions = svalue.split(",");
            var alls=[]
            for(var i in selectedsOptions) {
                var optionVal = selectedsOptions[i];
                alls.push(optionVal);
            }
             $("#medTechspeciality,.multiselect").val(alls).show();
             $("#medTechspeciality").multiselect('refresh');

            $("#medTechlicense").val($(row.children().find('span').get(4)).text());

        }
        function edit_medTech_data(id) {
            var fname = $("#medTechfname").val();
            var mname = $("#medTechmname").val();
            var lname = $("#medTechlname").val();
            var countryCode = $("#countrycodemed").val();
            var contactNo = $("#medTechcontact").val();
            var contact = countryCode + ' ' + contactNo;
            var gender = $("#medTechgender").val();
            var email = $("#medTechemail").val();

            var speciality = $("#medTechspeciality").val();
            if (speciality !== null) {
                var speciality = speciality.join();
            }
            else {
                var speciality = "";
            }
            var medTechqualification = $("#medTechqualification").val();
            if (medTechqualification !== null) {
                var medTechqualification = medTechqualification.join();
            }
            else {
                var medTechqualification = "";
            }
            var experiencemonth = $("#medTechexperience").val();
            var experienceyear = $("#selectYear").val();
            var experience = experienceyear + ' years ' + experiencemonth + ' months'
            // var experience = $("#nurseexperience").val();
            var branchCode = $("#branchcode").val();
            var license = $("#medTechlicense").val();
            if (fname == '') {
                $("#dialogboxmedTech").show();
                $("#errorMsgFname").html('First name is mandatory');
                $("#dialogboxmedTech").delay(4000).fadeOut();
            }
            else if (lname == '') {
                $("#dialogboxmedTech8").show();
                $("#errorMsglname").html('Last name is mandatory');
                $("#dialogboxmedTech8").delay(4000).fadeOut();
            }
            else if ( contactNo.length <= 9) {
                if (contactNo == '') {
                    
                    $("#dialogboxmedTech1").show();
                    $("#errorMsgContact").html('Contact number is mandatory');
                    $("#dialogboxmedTech1").delay(4000).fadeOut();
                }
                else if(contactNo.length < 10){
                    $("#dialogboxmedTech1").show();
                $("#errorMsgContact").html('Contact number should be 10 digits');
                $("#dialogboxmedTech1").delay(4000).fadeOut();
                
                }
            }
            else if (branchcode == null) {
                $("#dialogboxmedTech2").show();
                $("#errorMsgUsername").html('Branch Code is mandatory');
                $("#dialogboxmedTech2").delay(4000).fadeOut();
            }
            
            else if (speciality == '') {
                $("#dialogboxmedTech3").show();
                $("#errorMsgSpeciality").html('Speciality is mandatory');
                $("#dialogboxmedTech3").delay(4000).fadeOut();
            }
            else if (medTechqualification == '') {
                $("#dialogboxmedTech3").show();
                $("#errorMsgSpeciality").html('Qualification is mandatory');
                $("#dialogboxmedTech3").delay(4000).fadeOut();
            }
            else if (experience == '0 years 0 months') {
                $("#dialogboxmedTech4").show();
                $("#errorMsgExperience").html('Experience is mandatory');
                $("#dialogboxmedTech4").delay(4000).fadeOut();
            }
            else if (license == '') {
                $("#dialogboxmedTech5").show();
                $("#errorMsgLicense").html('License number is mandatory');
                $("#dialogboxmedTech5").delay(4000).fadeOut();
            }

            // }
            else {
            var medTech_data = {
                "staff": id,
                "pro": {

                    // "gender": gender,
                    "first_name": fname,
                    "middle_name": mname,
                    "last_name": lname,
                    "Qualification": medTechqualification,
                    "user_type": 5,
                    "phone": contact
                },
                "branch_code": branchCode,
                "speciality": speciality,
                "Experience": experience,
                "Licence_number": license
            }

            // console.log(medTech_data)
            update_staff(medTech_data, function (data, status) {
                if (status == "success") {

                    $("#medTechfname").val("");
                    $("#medTechmname").val("");
                    $("#medTechlname").val("");
                    $("#medTechcontact").val("");
                    $("#branchcode").val("");
                    $("#medTechgender,#medTechgendername").val("").show();
                    $("#medTechemailname,#medTechemailnamei").show();
                    $("#medTechqualification,#medTechspeciality").multiselect('clearSelection');
                    $("#medTechqualification,#medTechspeciality").multiselect('refresh');
                    $("#selectYear, #medTechexperience,#medTechexperiencenamen,#medTechexperience").val("0");
                    $("#medTechlicense").val("");
                    load_medTech();
                    dlg.dialog("close");
                }
            });
        }
    }
        function save_medTech_data() {
            // alert("save medtech function")
            var fname = $("#medTechfname").val();
            var mname = $("#medTechmname").val();
            var lname = $("#medTechlname").val();

            var countryCode = $("#countrycodemed").val();

            var contactNo = $("#medTechcontact").val();
            var contact = countryCode + ' ' + contactNo;
            var gender = $("#medTechgender").val();
            var email = $("#medTechemail").val();
            // var username = $("#nurseusername").val();
            var speciality = $("#medTechspeciality").val();
            if (speciality !== null) {
                var speciality = speciality.join();
            }
            else {
                var speciality = "";
            }
            var medTechqualification = $("#medTechqualification").val();
            if (medTechqualification !== null) {
                var medTechqualification = medTechqualification.join();
            }
            else {
                var medTechqualification = "";
            }
            var experiencemonth = $("#medTechexperience").val();
            var experienceyear = $("#selectYear").val();
            var experience = experienceyear + ' years ' + experiencemonth + ' months'
            var branchCode = $("#branchcode").val();
            var license = $("#medTechlicense").val();
            
            var atposition=email.indexOf("@");  
            var dotposition=email.lastIndexOf(".");  
            if (fname == '') {
                $("#dialogboxmedTech").show();
                $("#errorMsgFname").html('First name is mandatory');
                $("#dialogboxmedTech").delay(4000).fadeOut();
            }
            else if (lname == '') {
                $("#dialogboxmedTech8").show();
                $("#errorMsglname").html('Last name is mandatory');
                $("#dialogboxmedTech8").delay(4000).fadeOut();
            }
            else if ( contactNo.length <= 9) {
                if (contactNo == '') {
                    
                    $("#dialogboxmedTech1").show();
                    $("#errorMsgContact").html('Contact number is mandatory');
                    $("#dialogboxmedTech1").delay(4000).fadeOut();
                }
                else if(contactNo.length < 10){
                    $("#dialogboxmedTech1").show();
                $("#errorMsgContact").html('Contact number should be 10 digits');
                $("#dialogboxmedTech1").delay(4000).fadeOut();
                
                }
            }
            else if (gender == null) {
                $("#dialogboxmedTech7").show();
                $("#errorMsgemail").html('Gender is mandatory');
                $("#dialogboxmedTech7").delay(4000).fadeOut();
            }
            else if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length) {
                if (email == ''){
                $("#dialogboxmedTech7").show();
                $("#errorMsgemail").html('Email address is mandatory');
                $("#dialogboxmedTech7").delay(4000).fadeOut();
                }
                else {
                    $("#dialogboxmedTech7").show();
                    $("#errorMsgemail").html('Please enter a valid email address');
                    $("#dialogboxmedTech7").delay(4000).fadeOut();
                } 
            }

            else if (branchCode == null) {
                $("#dialogboxmedTech7").show();
                $("#errorMsgemail").html('Branch Code is mandatory');
                $("#dialogboxmedTech7").delay(4000).fadeOut();
            }
            
            else if (speciality == '') {
                $("#dialogboxmedTech3").show();
                $("#errorMsgSpeciality").html('Speciality is mandatory');
                $("#dialogboxmedTech3").delay(4000).fadeOut();
            }
            
            else if (license == '') {
                $("#dialogboxmedTech5").show();
                $("#errorMsgLicense").html('License number is mandatory');
                $("#dialogboxmedTech5").delay(4000).fadeOut();
            }
            else if (medTechqualification == '') {
                $("#dialogboxmedTech6").show();
                $("#errorMsgQualification").html('Qualification is mandatory');
                $("#dialogboxmedTech6").delay(4000).fadeOut();
            }
            else if (experience == '0 years 0 months') {
                $("#dialogboxmedTech4").show();
                $("#errorMsgExperience").html('Experience is mandatory');
                $("#dialogboxmedTech4").delay(4000).fadeOut();
            }
            // }
            else {


                var medTech_data = {

                    "email": email,
                    "gender": gender,
                    "first_name": fname,
                    "middle_name": mname,
                    "last_name": lname,
                    "Qualification": medTechqualification,
                    "user_type": 5,
                    "phone": contact,
                    "branch_code": branchCode,
                    "speciality": speciality,
                    "Experience": experience,
                    "Licence_number": license
                }
                // console.log(medTech_data);

                save_staff(medTech_data, function (data, status) {
                    if (status == "success") {
                        // alert("Created Save MedTech");
                        $("#medTechfname").val("");
                        $("#medTechmname").val("");
                        $("#medTechlname").val("");
                        $("#medTechcontact").val("");
                        $("#medTechgender,#medTechgender").val("").show();
                        $("#medTechemail,#medTechemailname").val("").show();
                        $("#branchcode").val("");
                        $('#medTechqualification,#medTechspeciality').multiselect('clearSelection');
                        $("#medTechqualification,#medTechspeciality").multiselect('refresh');
                        $("#medTechqualificationnamen,#medTechqualificationname").val("").show();
                        $("#medTechexperience,#selectYear").val("0").show();
                        $("#medTechlicense,#medTechlicensename").val(null).show();
                        load_medTech();
                        dlg.dialog("close");
                    }
                });
            }
        }
    };
    $(document).on('click', 'a.medTechdelete', function () {
        id = $(this).data('id');
        //        alert("delete ::"+id);
        delete_staff(id, function (data, status) {
            load_medTech();
        });
        return false;
    });

    $(document).on('click', 'td a.medTechedit', function () {
        new_dialog('Edit', $(this).parents('tr'), $(this).data('id'));
        return false;
    });
    $(".medTech-adduser").button().click(new_dialog);

    load_medTech();

});


/*org*/
$(function () {
    var load_organization = function () {
        get_organization_data(function (data, status) {
            // console.log('a');
            var organization_view = ""
            var organization_select_field = ""
            // console.log(data)
            if (data.length >= 0) {
                for (var i = 0; i < data.length; i++) {
                    // console.log(i);
                    var alr = data[i]
                    organization_view += '<tr >';
                    organization_view += '<td><span>' + alr.organization_name + '</span></td>';
                    organization_view += '<td><span>' + alr.organization_id + '</span></td>';
                    organization_view += '<td><span>' + alr.organization_address + '</span></td>'
                    organization_view += '</tr>';
                }
                $("#myorgTable").html(organization_view);
            }
            if (data.length >= 0) {
                organization_select_field += '<option value="" disabled selected>Select Distributor</option>'
                for (var i = 0; i < data.length; i++) {
                    var alr = data[i]
                    // console.log(alr);

                    organization_select_field += '<option value="' + alr.id + ' ">' + alr.organization_name + '</option>';


                }
                $("#organizationNames").html(organization_select_field);
            }
        });
    }
    var new_dialog = function (type, row, org_id) {
        var dlg = $("#organization-form");
        type = type || 'Create';
        var config = {
            autoOpen: true,
            height: 300,
            width: 786,
            modal: true,
            buttons: {
                "Create": save_org_data,
                "Cancel": function () {
                    dlg.dialog("close");
                    $("#organization_name").val("");
                    $("#organization_id").val("");
                    $("#organization_address").val("");
                }
            },
            close: function () {
                dlg.dialog("close");
            }
        };

        if (type === 'Edit') {
            get_org_data_for_edit(row);
            delete (config.buttons['Create']);
            config.buttons['Save'] = function () {
                edit_org_data(org_id)
                row.remove();
            };
            config.buttons['Cancel'] = function () {

                dlg.dialog("close");
            };
        }
        dlg.dialog(config);
        function get_org_data_for_edit(row) {

        }
        function edit_org_data(id) {

            var org_data = {
                "organization_name": organization_name,
                "organization_id": organization_id,
                "organization_address": organization_address,
            }
            // console.log("", org_data)
            update_org(org_data, function (data, status) {
                if (status == "success") {

                    dlg.dialog("close");

                }
            });
        }

        function save_org_data() {
            var organization_name = $("#organization_name").val();
            var organization_id = $("#organization_id").val();
            var organization_address = $("#organization_address").val();
            // console.log(organization_name);
            // console.log(organization_id);
            if (organization_name == '') {
                $("#dialogbox").show();
                $("#errorMsg").html('Distributor name is mandatory');
                $("#dialogbox").delay(4000).fadeOut();
            }
            else if (organization_id == '') {
                $("#dialogbox").show();
                $("#errorMsg").html('Distributor code is mandatory');
                $("#dialogbox").delay(4000).fadeOut();
            }
            else if(organization_address == ''){
                $("#dialogbox").show();
                $("#errorMsg").html('Distributor Address is mandatory');
                $("#dialogbox").delay(4000).fadeOut();
            }

            else {
                var org_data = {
                    "organization_name": organization_name,
                    "organization_id": organization_id,
                    "organization_address": organization_address,
                }

                save_org(org_data, function (data, status) {
                    if (status == "success") {
                        $("#organization_name").val("");
                        $("#organization_id").val("");
                        $("#organization_address").val("");
                        load_organization();

                        dlg.dialog("close");
                    }
                });
            }
        }
    };


    $(document).on('click', 'a.orgdelete', function () {
        id = $(this).data('id');
        //        alert("delete ::"+id);
        delete_staff(id, function (data, status) {
            load_organization();
        });
        return false;
    });
    $(document).on('click', 'td a.orgedit', function () {
        new_dialog('Edit', $(this).parents('tr'), $(this).data('id'));
        return false;
    });
    $(".org-add").button().click(new_dialog);

    load_organization();

});
/*branch*/

$(function () {
    var load_branch = function () {
        get_branches_data(function (data, status) {
            var branch_view = ""
            var branch_select_field = ""
	    var branchcodenamehr =""
            // console.log(data)
            if (data.length >= 0) {
                for (var i = 0; i < data.length; i++) {
                    var alr = data[i]
                    // console.log(alr);
                    branch_view += '<tr >';
                    branch_view += '<td><span>' + alr.branch_name + '</span></td>';
                    branch_view += '<td><span>' + alr.branch_code + '</span></td>';
                    branch_view += '<td><span>' + alr.branch_address + '</span></td>';




                    branch_view += '</tr>';
                }
                $("#mybranchTable").html(branch_view);
                if (data.length >= 0) {
                    branch_select_field += '<option value="" selected disabled>Select Branch</option>'
		    branchcodenamehr += '<option value="" selected disabled>Select Branch</option>'

                    for (var i = 0; i < data.length; i++) {
                        var alr = data[i]
                        // console.log(alr);

                        branch_select_field += '<option value="' + alr.id + ' ">' + alr.branch_code + '</option>';
			branchcodenamehr += '<option value="' + alr.branch_code+ '">' + alr.branch_code + '</option>';




                    }
                    $("#corpbranchNames").html(branch_select_field);
		    $("#branchcodehr").html(branchcodenamehr);
                }



            }
        });
    }
    var new_dialog = function (type, row, org_id) {
        var dlg = $("#branch-form");
        type = type || 'Create';
        var config = {
            autoOpen: true,
            height: 300,
            width: 786,
            modal: true,
            buttons: {
                "Create": save_branch_data,
                "Cancel": function () {
                    dlg.dialog("close");
                    $("#organizationNames").val("");
                    $("#branch_name").val("");
                    $("#branch_address").val("");
                }
            },
            close: function () {
                dlg.dialog("close");
            }
        };

        if (type === 'Edit') {
            get_branch_data_for_edit(row);
            delete (config.buttons['Create']);
            config.buttons['Save'] = function () {
                edit_org_data(org_id)
                row.remove();
            };
            config.buttons['Cancel'] = function () {
                dlg.dialog("close");
                $("#organizationNames").val("");
                $("#branch_name").val("");
                $("#branch_address").val("");
            };
        }
        dlg.dialog(config);
        function get_branch_data_for_edit(row) {
        }
        function edit_branch_data(id) {
            var org_data = {
                "organaisation_code": organizationNames,
                "branch_name": branch_name,
                "branch_address": branch_address,





            }
            // console.log("", org_data)
            update_org(org_data, function (data, status) {
                if (status == "success") {
                    dlg.dialog("close");
                    $("#organizationNames").val("");
                    $("#branch_name").val("");
                    $("#branch_address").val("");
                }
            });
        }
        function save_branch_data() {
            var organizationNames = $("#organizationNames").val();
            var branch_name = $("#branch_name").val();
            var branch_address = $("#branch_address").val();
            // console.log(organizationNames);
            // console.log(branch_name);
            if (organizationNames == null) {
                $("#dialogbox").show();
                $("#errorMsg").html('Distributor name is mandatory');
                $("#dialogbox").delay(4000).fadeOut();
            }
            else if (branch_name == '') {
                $("#dialogbox").show();
                $("#errorMsg").html('Branch name is mandatory');
                $("#dialogbox").delay(4000).fadeOut();
            }
            else if(branch_address == ''){
                $("#dialogbox").show();
                $("#errorMsg").html('Branch address is mandatory');
                $("#dialogbox").delay(4000).fadeOut();
            }

            else {
                var branch_data = {
                    "organaisation_code": organizationNames,
                    "branch_name": branch_name,
                    "branch_address": branch_address,
                }
                save_branch(branch_data, function (data, status) {
                    if (status == "success") {
                        $("#organizationNames").val("");
                        $("#branch_name").val("");
                        $("#branch_address").val("");
                        load_branch();
                        dlg.dialog("close");
                    }
                });
            }
        }
    };


    $(document).on('click', 'a.orgdelete', function () {
        id = $(this).data('id');
        //        alert("delete ::"+id);
        delete_staff(id, function (data, status) {
            load_branch();
        });
        return false;
    });
    $(document).on('click', 'td a.orgedit', function () {
        new_dialog('Edit', $(this).parents('tr'), $(this).data('id'));
        return false;
    });
    $(".branch-add").button().click(new_dialog);

    load_branch();

});
/*corporate org*/
$(function () {
    var load_corp = function () {
        get_corporate_data(function (data, status) {
            var corp_view = ""
            var corp_select_view = ""
            // console.log(data)
            if (data.length >= 0) {
                corp_select_view += '<option value="" selected disabled>Select</option>';

                for (var i = 0; i < data.length; i++) {
                    var alr = data[i]
                    // console.log(alr);
                    corp_view += '<tr >';
                    corp_view += '<td><span>' + alr.corporate_name + '</span></td>';
                    corp_view += '<td><span>' + alr.corporate_code + '</span></td>';
                    corp_view += '<td><span>' + alr.number_of_visits + '</span></td>';

                    corp_view += '<td><span>' + alr.corporate_branch_address + '</span></td>';
                    corp_view += '</tr>';


                    corp_select_view += '<option value="' + alr.corporate_code + '">' + alr.corporate_code + '</option>';

                }
                $("#mycorpTable").html(corp_view);
                $("#corpCodeSelectField").html(corp_select_view);

            }
        });
    }
    var new_dialog = function (type, row, org_id) {
        var dlg = $("#corpbranch-form");
        type = type || 'Create';
        var config = {
            autoOpen: true,
            height: 300,
            width: 786,
            modal: true,
            buttons: {
                "Create": save_branch_data,
                "Cancel": function () {
                    dlg.dialog("close");
//                    $("#corpbranchNames").val("");
                    $("#corp_name").val("");
                    $("#corp_code").val("");
                    $("#corp_address").val("");
		    $("#nofvisits").val("");

			

                }
            },
            close: function () {
                dlg.dialog("close");
            }
        };

        if (type === 'Edit') {
            get_branch_data_for_edit(row);
            delete (config.buttons['Create']);
            config.buttons['Save'] = function () {
                edit_org_data(org_id)
                row.remove();
            };
            config.buttons['Cancel'] = function () {
                dlg.dialog("close");
            };
        }
        dlg.dialog(config);
        function get_branch_data_for_edit(row) {
        }
        function edit_branch_data(id) {
            var org_data = {
                "organaisation_code": organizationNames,
                "branch_name": branch_name,
            }
            // console.log("", org_data)
            update_org(org_data, function (data, status) {
                if (status == "success") {

                    dlg.dialog("close");
                }
            });
        }
        function save_branch_data() {
//            var corpbranchNames = $("#corpbranchNames").val();
            var corp_name = $("#corp_name").val();
            var corp_code = $("#corp_code").val();
            var corp_address = $("#corp_address").val();
            var nofvisits = $("#nofvisits").val();
            // console.log(corp_address);


            // console.log(corp_name);

//            if (corpbranchNames == null) {
//                $("#dialogbox").show();
//                $("#errorMsg").html('Branch code is mandatory');
//                $("#dialogbox").delay(4000).fadeOut();
//            }
            if (corp_name == '') {
                $("#dialogbox").show();
                $("#errorMsg").html('Corporate name is mandatory');
                $("#dialogbox").delay(4000).fadeOut();
            }
            else if (corp_code == '') {
                $("#dialogbox").show();
                $("#errorMsg").html('Corporate code is mandatory');
                $("#dialogbox").delay(4000).fadeOut();
            }
            else if(corp_address== ''){
                $("#dialogbox").show();
                $("#errorMsg").html('Corporate branch address is mandatory');
                $("#dialogbox").delay(4000).fadeOut();
            }
            else if(nofvisits== ''){
                $("#dialogbox").show();
                $("#errorMsg").html('Corporate branch address is mandatory');
                $("#dialogbox").delay(4000).fadeOut();
            }

            else {
                var corp_data = {
                    "corporate_name": corp_name,
                    "corporate_code": corp_code,
                    "corporate_branch_address": corp_address,
                    "number_of_visits": nofvisits
                }
                save_corp(corp_data, function (data, status) {
                    if (status == "success") {

                        $("#corp_name").val("");
                        $("#corp_code").val("");
                        $("#corp_address").val("");
			$("#nofvisits").val("");


                        load_corp();

                        dlg.dialog("close");

                    }
                });
            }
        }
    };


    $(document).on('click', 'a.corpdelete', function () {
        id = $(this).data('id');
        //        alert("delete ::"+id);
        delete_staff(id, function (data, status) {
            load_corp();
        });
        return false;
    });
    $(document).on('click', 'td a.corpedit', function () {
        new_dialog('Edit', $(this).parents('tr'), $(this).data('id'));
        return false;
    });
    $(".corp_branch-add").button().click(new_dialog);

    load_corp();

});

/*corp_HR*/
$(function () {
    var load_corphr = function () {
        get_corphr_data(function (data, status) {
            var corphr_view = ""
            // console.log("get corporate hr data", data)
            if (data.length >= 0) {
                for (var i = 0; i < data.length; i++) {
                    var alr = data[i]
                    corphr_view += '<tr >';
                    corphr_view += '<td><span>' + alr.pro.first_name + ' ' + '</span><span>' + alr.pro.middle_name + ' ' + '</span><span>' + alr.pro.last_name + '</span></td>';
                    corphr_view += '<td><span>' + alr.employee_code + '</span></td>';
                    corphr_view += '<td><span>' + alr.branch_code + '</span><span style="display: none;">' + alr.pro.gender + '</span><span style="display: none;">' + alr.pro.phone + '</span></td>';
                    // alert(alr.pro.phone)
                    var a = alr.pro.phone.split(" ");
                    var phon = a[1]
                    // console.log("phone number " + phon)
                    corphr_view += '<td style="display: none;"><span>' +phon+'</span></td>'
		    corphr_view += '<td style="display: none;"><span>'+alr.Designation +'</span></td>' 
		    corphr_view += '<td ><span>'+alr.branch_name +'</span></td>'
                    corphr_view += '<td ><a style="color: #64c1b1; " href="/corporatehrprofile/' + alr.hr.id + '/"class="fa fa-user-circle fa-lg" ></a></td>';
                    if(suser=="superadmin"){
                        corphr_view += '<td style="display:none"><a style="color: #64c1b1; " href="javascript:void(0)" data-id="' + alr.hr.id + '" class="corphredit fa fa-pencil-square-o "></a> </td>';
                        corphr_view += '<td style="display:none"><a style="color: #64c1b1; ;"  href="javascript:void(0)" data-id="' + alr.hr.id + '" class="corphrdelete fa fa-trash-o"></a></td>';
                    }
                    else{
                        corphr_view += '<td><a style="color: #64c1b1; " href="javascript:void(0)" data-id="' + alr.hr.id + '" class="corphredit fa fa-pencil-square-o "></a> </td>';
                        corphr_view += '<td><a style="color: #64c1b1; ;"  href="javascript:void(0)" data-id="' + alr.hr.id + '" class="corphrdelete fa fa-trash-o"></a></td>';
                    }
                    corphr_view += '</tr>';
                }
                $("#CorpTable").html(corphr_view);
            }
        });
    }
    var new_dialog = function (type, row, corp_hr_id) {
        var dlg = $("#corphr-form");
        type = type || 'Create';
        var config = {
            autoOpen: true,
            height: 300,
            width: 786,
            modal: true,
            buttons: {
                "Create": save_corphr_data,
                "Cancel": function () {
                    dlg.dialog("close");
                    $("#corpfname").val('');
                    $("#corpmname").val('');
                    $("#corplname").val('');
                    $("#corpcontact_num").val('');
                    $("#corpdocgender").val('');
                    $("#corpbranch").val('');
                    $("#emplcode").val('');
                    $("#corpdesig").val('');
		    $("#branchcodehr").val('');
                    $("#corpCodeSelectField,#corpemail").val("").show();


                    // $("#docqualification").val([]);

                    load_corphr();

                    dlg.dialog("close");
                }
            },
            close: function () {
                dlg.dialog("close");
            }
        };

        if (type === 'Edit') {
            get_corphr_data_for_edit(row);
            delete (config.buttons['Create']);
            config.buttons['Save'] = function () {
                edit_corphr_data(corp_hr_id)
                row.remove();
            };
            config.buttons['Cancel'] = function () {
                $("#corpfname").val('');
                $("#corpmname").val('');
                $("#corplname").val('');
                $("#corpcontact_num").val('');
                $("#corpdocgender,#corpgendername,#corpogenderrvalue").val('').show();
                $("#corpCodeSelectField").val('');
                $("#emplcode").val('');
                $("#corpdesig").val('');

                $("#corpemaillabel,#corpemail1").val("").show();

                load_corphr();
                dlg.dialog("close");
            };
        }
        dlg.dialog(config);
        function get_corphr_data_for_edit(row) {
            $("#corpfname").val($(row.children().find('span').get(0)).text());
            $("#corpmname").val($(row.children().find('span').get(1)).text());
            $("#corplname").val($(row.children().find('span').get(2)).text());
            $("#corpdesig").val($(row.children().find('span').get(8)).text());
	    $("#branchcodehr").val($(row.children().find('span').get(9)).text());
            // alert($(row.children().find('span').get(7)).text())
            $("#corpcontact_num").val($(row.children().find('span').get(7)).text());
            $("#corpdocgender,#corpgendername,#corpogenderrvalue").val($(row.children().find('span').get(5)).text()).hide();
            $("#corpCodeSelectField").val($(row.children().find('span').get(4)).text());
            $("#emplcode").val($(row.children().find('span').get(3)).text());
            $("#corpemaillabel,#corpemail1").hide();


        }
        function edit_corphr_data(id) {
            var fname = $("#corpfname").val();
            var mname = $("#corpmname").val();
            var lname = $("#corplname").val();
            var countryCode = $("#corpcontact_code").val();
            var contactNo = $("#corpcontact_num").val();
            var contact = countryCode + ' ' + contactNo;
            // console.log(contact)
            var gender = $("#corpdocgender").val();
            var email = $("#corpemail").val();
            var branchCode = $("#corpCodeSelectField").val();
            var employee_code = $("#emplcode").val();
            var corpdesig = $("#corpdesig").val();
	    var branchname = $("#branchcodehr").val();



            var corphr_data = {
                "hr": {
                    "id": id,

                },
                "pro": {
                    // "gender": gender,
                    "first_name": fname,
                    "middle_name": mname,
                    "last_name": lname,
                    "Qualification": "",
                    "user_type": 6,
                    "phone": contact
                },
                "branch_code": branchCode,
		"branch_name": branchname,
                "employee_code": employee_code,
                "Designation": corpdesig
            }
            // console.log("", corphr_data)
            update_corphr(corphr_data, function (data, status) {
                if (status == "success") {
                    $("#corpfname").val('');
                    $("#corpmname").val('');
                    $("#corplname").val('');
                    $("#corpcontact_num").val('');
                    $("#corpdocgender,#corpgendername,#corpogenderrvalue").val('').show();
                    $("#corpCodeSelectField").val('');
                    $("#emplcode").val('');
                    $("#corpdesig").val('');
		    $("#branchcodehr").val("");
		    $("#branchcodehr").val("");
                    $("#corpemaillabel,#corpemail1").val("").show();

                    load_corphr();
                    dlg.dialog("close");

                }
            });
        }

        function save_corphr_data() {

            var fname = $("#corpfname").val();
            var mname = $("#corpmname").val();
            var lname = $("#corplname").val();

            var countryCode = $("#corpcontact_code").val();
            var contactNo = $("#corpcontact_num").val();
            var contact = countryCode + ' ' + contactNo;
            // console.log(contact)
            var gender = $("#corpdocgender").val();
            var email = $("#corpemail").val();
            var branchCode = $("#corpCodeSelectField").val();
            var employee_code = $("#emplcode").val();
            var corpdesig = $("#corpdesig").val();
	    var branchname = $("#branchcodehr").val();

            var atposition=email.indexOf("@");  
            var dotposition=email.lastIndexOf(".");

                       if (fname == '') {
                           $("#dialogbox").show();
                           $("#errorMsg").html('First name is mandatory');
                           $("#dialogbox").delay(4000).fadeOut();
                       }
                       else if (lname == '') {
                        $("#dialogbox").show();
                        $("#errorMsg").html('Last name is mandatory');
                        $("#dialogbox").delay(4000).fadeOut();
                       }
                       else if(employee_code == ''){
                        $("#dialogbox").show();
                        $("#errorMsg").html('Employee code is mandatory');
                        $("#dialogbox").delay(4000).fadeOut();
                       }
                       else if(corpdesig == ''){
                        $("#dialogbox").show();
                        $("#errorMsg").html('Designation is mandatory');
                        $("#dialogbox").delay(4000).fadeOut();
                       }

                       else if ( contactNo.length <= 9) {
                            if (contactNo == '') {
                                $("#dialogbox").show();
                                $("#errorMsg").html('Contact number is mandatory');
                                $("#dialogbox").delay(4000).fadeOut();
                            }
                            else if(contactNo.length <10){
                                $("#dialogbox").show();
                                $("#errorMsg").html('Contact number should be 10 digits');
                                $("#dialogbox").delay(4000).fadeOut();
                            }
                        }
                        else if(gender == null){
                            $("#dialogbox").show();
                            $("#errorMsg").html('Gender is mandatory');
                            $("#dialogbox").delay(4000).fadeOut();
                        }
			else if(branchname == null){
                            $("#dialogbox").show();
                            $("#errorMsg").html('Branch code is mandatory');
                            $("#dialogbox").delay(4000).fadeOut();
                        }

                        
                        else if (branchCode == null) {
                            $("#dialogbox").show();
                            $("#errorMsg").html('Corporate branch code is mandatory');
                            $("#dialogbox").delay(4000).fadeOut();
                        }
                        else if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length) {
                            if (email == ''){
                                $("#dialogbox").show();
                                $("#errorMsg").html('Email is mandatory');
                                $("#dialogbox").delay(4000).fadeOut();
                            }
                            else {
                                $("#dialogbox").show();
                                $("#errorMsg").html('Please enter a valid email address');
                                $("#dialogbox").delay(4000).fadeOut();
                            }
                        }
                       else {

            var corp_hr_data = {


                "email": email,
                "gender": gender,
                "first_name": fname,
                "middle_name": mname,
                "last_name": lname,
                "Qualification": " ",
                "user_type": 6,
                "phone": contact,
                "Designation":corpdesig,
		"branch_name":branchname,
                "employee_code": employee_code,
                "branch_code": branchCode


            }

            console.log(corp_hr_data);
            save_corp_hr(corp_hr_data, function (data, status) {
                if (status == "success") {
                    $("#corpfname").val('');
                    $("#corpmname").val('');
                    $("#corplname").val('');
                    $("#corpcontact_num").val('');
                    $("#corpdocgender").val('');
                    $("#corpbranch").val('');
                    $("#corpdesig").val('');
		    $("#branchcodehr").val('');
                    $("#emplcode").val('');
                    $("#corpCodeSelectField,#corpemail").val("").show();


                    // $("#docqualification").val([]);

                    load_corphr();

                    dlg.dialog("close");
                }
            });
        }
        }
    };


    $(document).on('click', 'a.corphrdelete', function () {
        id = $(this).data('id');
        // alert("delete ::" + id);
        delete_corphr(id, function (data, status) {
            load_corphr();
        });
        return false;
    });
    $(document).on('click', 'td a.corphredit', function () {
        new_dialog('Edit', $(this).parents('tr'), $(this).data('id'));
        return false;
    });
    $(".corphr-adduser").button().click(new_dialog);

    load_corphr();

});

/* get patients */
