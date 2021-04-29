import $ from "jquery";

function checkIsCSU() {
    $("#isCSU")
        .change(function () {
            $("#CSU_info").toggle(this.checked);
        })
        .change();
}
