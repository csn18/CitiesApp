
let countryId = '';

function ajaxPagination() {
  $('#pagination a.page-link').each((index, el) => {
      $(el).click((e) => {
          e.preventDefault();
            let getHrefSplit = $(el).attr('href').split('&')[1]
            countryId = countryId ? countryId : $(el).attr('href').split('=')[1][0];
            let pageUrl = `?countries_id=${countryId}&${getHrefSplit}`

          $.ajax({
              url: pageUrl,
              type: 'GET',
              success: (data) => {
                  $('#cities').empty();
                  $('#cities').append( $(data).find('#cities') );


                  $('#pagination').empty();
                  $('#pagination').append( $(data).find('#pagination').html() );
              }
          })
      })
  })
}


function ajaxSearch() {
  $(document).ready(function(){
    $('#searchBox').on('input', function(e){
      textInSearchBox = $('#searchBox').val();

      $.ajax({
        url: '/task6search',
        type: 'POST',
        data: {text: textInSearchBox},
        success: (result) => {
          countryId = result['countryId']
          res = result['cities']


          if(result) {
            $('#listGroup').empty();
            for (let i = 0; i < 5; i++) {
            $('#listGroup').append(`<li class="list-group-item">${res[i]}</li>`)
            }
          }
        }
      })
    })
  })
}


originalOnload = window.onload;
window.onload = function() {
  if (originalOnload) {
    originalOnload();
  }
    $(document).ready(function() {
    ajaxPagination()
    })

    $(document).ajaxStop(function() {
      ajaxPagination()
    })

    $(document).ready(function(){
    ajaxSearch()
    })
};