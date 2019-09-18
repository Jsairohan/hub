$(function () {
    var load_patients = function () {
        // var treated = ''
        if (treated ==1 && type=="Corporate"){
            data="/patients/?patient_type=Corporate&istreated=1"
            

        }
        else if(treated ==0  && type=="Corporate"){
           
            data="/patients/?patient_type=Corporate&istreated=0"
        }
        else if(treated==1 &&   type=="docinpat" ){
            // data="/patientcops/"
            data ="/patients/?istreated=1"
        }
        else if(treated==0 && type=="docinpat"){
            // data="/patientcops/"
            data ="/patients/?istreated=0"
        }
        else if(treated==2 && type=="unassign"){
            // data="/patientcops/"
            data ="/patients/?patient_type=Corporate"
        }
       

       getpatients(data,function (data, status) {
          
            var patients_view = ""
            var patients_view_in_hr = ""
           
            if (data.length >= 0) {

                for (var i = 0; i < data.length; i++) {
                    var alr = data[i]
                    patients_view += '<tr >';
                    patients_view += '<td ><span>' + alr.pro.first_name + " " + '</span><span>' + alr.pro.middle_name + " " + '</span><span>' + alr.pro.last_name + '</span></td>';
                    patients_view += '<td ><span>' + alr.PHID + '</span></td>';
                    patients_view += '<td style="display: none;" ><span>' + alr.pro.gender + '</span></td>'
                    patients_view += '<td style="display: none;" ><span>' + alr.pro.Qualification + '</span></td>';;
                    patients_view += '<td style="display: none;" ><span>' + alr.pro.phone + '</span></td>';
                    patients_view += '<td style="display: none;" ><span>' + alr.pro.gender + '</span></td>';
                    var a = alr.pro.phone.split(" ");
                    var phon = a[1]
                    patients_view += '<td style="display: none;" ><span>' + phon + '</span></td>';
                    // nurse_view += '<td style="display: none;" ><span>' + alr.nurse_user.username + '</span></td>';
                    patients_view += '<td style="display: none;"><span>' + alr.pat.email + '</span></td>';
                    
                    patients_view += '<td ><a style="color: #64c1b1; " href="/patientsummary/' + alr.pat.id + '/" class="fa fa-file-text fa-lg" ></a></td>';
                    // if(treated==1){
                        // patients_view +='<td>'+data.treatedOn+'</td>'
                        // patients_view +='<td>'+"data.treatedOn"+'</td>'
                    // }
                    patients_view += '</tr>';
                }
                $("#patientDataTable").html(patients_view)
                
                for (var i = 0; i < data.length; i++) {
                    var alr = data[i]
                    patients_view_in_hr += '<tr >';
                    patients_view_in_hr += '<td ><span>' + alr.pro.first_name + " " + '</span><span>' + alr.pro.middle_name + " " + '</span><span>' + alr.pro.last_name + '</span></td>';
                    patients_view_in_hr += '<td ><span>' + alr.PHID + '</span></td>';
                    patients_view_in_hr += '<td style="display: none;" ><span>' + alr.pro.gender + '</span></td>'
                    patients_view_in_hr += '<td style="display: none;" ><span>' + alr.pro.Qualification + '</span></td>';;
                    patients_view_in_hr += '<td style="display: none;" ><span>' + alr.pro.phone + '</span></td>';
                    patients_view_in_hr += '<td style="display: none;" ><span>' + alr.pro.gender + '</span></td>';
                    var a = alr.pro.phone.split(" ");
                    var phon = a[1]
                    patients_view_in_hr += '<td style="display: none;" ><span>' + phon + '</span></td>';
                    // nurse_view += '<td style="display: none;" ><span>' + alr.nurse_user.username + '</span></td>';
                    patients_view_in_hr += '<td style="display: none;"><span>' + alr.pat.email + '</span></td>';
                    if( treated==2 && type=="unassign"){
                    patients_view_in_hr += '<td style="display:none" ><a style="color: #64c1b1; "   href="/patientsummary/'+ alr.pat.id + '/"  class="fa fa-file-text fa-lg" ></a></td>';
                    }
                    else{
                        patients_view_in_hr += '<td ><a style="color: #64c1b1; "   href="/patientsummary/'+ alr.pat.id + '/"  class="fa fa-file-text fa-lg" ></a></td>';
                    }

                    patients_view_in_hr += '</tr>';
                }
                $("#patientDataTableInhr").html(patients_view_in_hr)
            }

            //
            
        });
    }
    load_patients();
});