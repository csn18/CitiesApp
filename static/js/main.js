
let countryId = '';

function ajaxPagination() {
  $('#pagination a.page-link').each((index, el) => {
      $(el).click((e) => {
          e.preventDefault();
            let getHrefSplit = $(el).attr('href').split('&')[1]
            let pageUrl = `?countries_id=${countryId}&${getHrefSplit}`
            console.log(getHrefSplit)

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
};