$(document).ready(function () {
  $("input#btn_translate").click(function () {
    let lang = $("input#language_code").val();
    let url = "https://hellosalut.stefanbohacek.dev";
    $.post(url, { lang: lang }).done(function (data) {
      $("div#hello").text(data["hello"]);
    });
  });
});
