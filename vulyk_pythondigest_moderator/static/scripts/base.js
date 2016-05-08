$(function () {
    var template = Handlebars.compile($('#names_template').html()),
        output = $("#out"),
        res = output.find("input[name=result]");

    $(document).bind('keydown', '1', function () {
        $(".selection button").eq(0).click();
    }).bind('keydown', '2', function () {
        $(".selection button").eq(1).click();
    });

    $(document.body).on("vulyk.next", function (e, data) {
        output.html(template(data.result.task.data));
        res.val("");
    }).on("vulyk.save", function (e, callback) {
        callback(res.serializeJSON());
        $("html, body").animate({scrollTop: 0}, "slow");
    }).on("click", ".selection button", function (e) {
        var el = $(this).closest("button");
        res.val(el.data("value"));
        $("a#save-button").click();
    }).on("vulyk.skip", function (e, callback) {
        callback();
        $("html, body").animate({scrollTop: 0}, "slow");
    }).on("vulyk.task_error", function (e, data) {
        $.magnificPopup.open({
            items: {
                src: '<div class="zoom-anim-dialog small-dialog">' +
                '<div class="dialog-content">Спасибо! Все задачи выполнены, но очень скоро мы добавим новые.</div>' +
                '</div>',
                type: 'inline'
            }
        })
    });
});
