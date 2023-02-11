$(document).ready(function () {
  show_detail();
});

function show_detail() {
  $('.detail_title').empty()
  $.ajax({
    type: "GET",
    url: "/showdetail",
    data: {},
    success: function (response) {
      let breadcontents = response
      console.log(breadcontents['contents'].length)
      for (let i = 0; i < breadcontents['contents'].length; i++) {
        let title = breadcontents['contents'][i]['title']
        let address = breadcontents['contents'][i]["address"]
        let best_bread = breadcontents['contents'][i]["best_bread"]
        let day = breadcontents['contents'][i]["day"]
        let image = breadcontents['contents'][i]["image"]
        let name = breadcontents['contents'][i]["name"]
        let num = breadcontents['contents'][i]["num"]
        let number = breadcontents['contents'][i]["number"]
        let star = breadcontents['contents'][i]["star"]

        let temp_title = `<h5>상호명:${title}</h5>`
        $('.detail_title').append(temp_title);


        let temp_best_bread = `<h5>대표빵:${best_bread}</h5>`
        $('.detail_bestbread').append(temp_best_bread);

        let temp_detail_contents = `<ul class="list-group">
                                    <li class="list-group-item">작성자:${name}</li>
                                    <li class="list-group-item">상호명:${title}</li>
                                    <li class="list-group-item">평점:${star}</li>
                                    <li class="list-group-item">주소:${address}</li>
                                    <li class="list-group-item">전화번호:${number}</li>
                                    <li class="list-group-item">휴무날:${day}</li>
                                  </ul>`
        $('.detail_contents').append(temp_detail_contents);

      }
    }
  });
}