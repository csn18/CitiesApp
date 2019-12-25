
function ajaxPagination() {
    $('#pagination a.page-link').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault();
            let page_url = $(el).attr('href');
            console.log( page_url );

            $.ajax({
                url: page_url,
                type: 'GET',
                success: (data) => {
                    $('#city').empty();
                    $('#city').append( $(data).find('#city') );


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
