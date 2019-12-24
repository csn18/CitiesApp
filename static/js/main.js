
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
 

function ajaxDropdown() {
  $('#dropdown a.dropdown-item').each((index, el) => {
      $(el).click((e) => {
          e.preventDefault();
          let getHref = $(el).attr('href')
          console.log(getHref)

          $.ajax({
            url: '/task6dropdown',
            type: 'GET',
            success: (result) => {
              countryId = result['countryId']
              country = result['country']
              console.log(countryId)
              console.log(country)

              $('#dropdown').empty()
              for (let i = 0; i < 5; i++) {
              $('#dropdown').append(`<a class="dropdown-item" href="?countries_id=${countryId}">${country}</a>`)}            }
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
    ajaxDropdown()
    })

  $(document).ready(function() {
    ajaxSearch()
    })
  
  $(document).ready(function() {
    ajaxPagination()
  })

    $(document).ajaxStop(function() {
      ajaxPagination()
    })
};
