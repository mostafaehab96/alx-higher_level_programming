$(document).ready(function () {
  $("input#btn_translate").click(translate);
  $("input#language_code").focus(function () {
    $(this).keypress(function (event) {
      if (event.which === 13) {
        translate();
      }
    });
  });
});

function translate() {
  let lang = $("input#language_code").val();
  let url = "https://hellosalut.stefanbohacek.dev";
  $.post(url, { lang: lang }).done(function (data) {
    $("div#hello").text(data["hello"]);
  });
}
