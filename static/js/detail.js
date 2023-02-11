let articles_pk = document.querySelector('#articles_pk').textContent
function deletepage(articles_pk) {
  $.ajax({
    type: "POST",
    url: "/detail/delete",
    data: {
      deletepk_give: articles_pk,
    },
    success: function (response) {
      alert(response["msg"]);
      window.location.href = '/';
    },
  });
}