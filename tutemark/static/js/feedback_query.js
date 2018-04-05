var default_options = {
    feedback_url : "",
    position : "left-top",
    jQueryUI : false,
    bootstrap : false,
    show_email : false,
    show_radio_button_list : false,
    close_on_click_outisde: true,
    name_label : "Name",
    email_label : "Email",
    message_label : "Message",
    radio_button_list_labels : ["1", "2", "3", "4", "5"],
    radio_button_list_title : "How would you rate my site?",
    name_placeholder : "",
    email_placeholder : "",
    message_placeholder : "",
    name_required : false,
    email_required : false,
    message_required : false,
    radio_button_list_required : false,
    show_asterisk_for_required : false,
    submit_label : "Send",
    title_label : "Feedback",
    trigger_label : "Feedback",
    custom_params : {},
    iframe_url : undefined,
    show_form: true,
    custom_html: "",
    delayed_close : true,
    delayed_options : {
        delay_success_milliseconds : 2000,
        delay_fail_milliseconds : 2000,
        sending : "Sending...",
        send_fail : "Sending failed.",
        send_success : "Feedack sent.",
        fail_color : undefined,
        success_color : undefined
    }
};

$(document).ready(function(){
    fm_options = {
        jQueryUI : true,
        position : "left-bottom",
        name_placeholder:"Name please",                     
        trigger_label : "Click me",
        message_required : true,
        show_asterisk_for_required : true,
        feedback_url : "send_feedback"
    };

    fm.init(fm_options);
});