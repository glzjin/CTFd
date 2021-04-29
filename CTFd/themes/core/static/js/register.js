import $ from "jquery";


$(() => {
    $("#mail_useauth")
        .change(function () {
            $("#mail_username_password").toggle(this.checked);
        })
        .change();
});
