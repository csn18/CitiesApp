'use strict';


let countryId = '';
let cities = '';


function ajaxPagination() {
    $('#pagination a.page-link').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault();
            let getHrefSplit = $(el).attr('href').split('&')[1];
            countryId = countryId ? countryId : $(el).attr('href').split('=')[1][0];
            let pageUrl = `?countries_id=${countryId}&${getHrefSplit}`;

            $.ajax({
                url: pageUrl,
                type: 'GET',
                success: (data) => {
                    $('#cities').empty();
                    $('#cities').append($(data).find('#cities'));


                    $('#pagination').empty();
                    $('#pagination').append($(data).find('#pagination').html());
                }
            })
        })
    })
}


function ajaxSearch() {
    $(document).ready(function () {
        $('#searchBox').on('input', function (e) {
            let textInSearchBox;
            textInSearchBox = $('#searchBox').val();


            $.ajax({
                url: '/search',
                type: 'GET',
                data: {text: textInSearchBox},
                success: (result) => {
                    countryId = result['countryId'];
                    cities = result['cities'];
                    initMap();


                    if (result) {
                        $('#listGroup').empty();
                        for (let i = 0; i < 5; i++) {
                            $('#listGroup').append(`<li class="list-group-item">${cities[i]}</li>`)
                        }
                    }
                }
            })
        })
    })
}


function initMap() {
    let opt = {
        center: {lat: 0, lng: 0},
        zoom: 2
    };

    geocode();

    function geocode() {
        let myMap = new google.maps.Map(document.getElementById('map'), opt);
        let apiKey = 'AIzaSyAJSa41jnaiHI4OD54Vg507O0qQKcXeY-0';
        for (let nameCity of cities) {
            axios.get('https://maps.googleapis.com/maps/api/geocode/json', {
                params: {
                    address: nameCity[0],
                    key: apiKey
                }
            }).then(function (response) {


                let lat = response.data.results[0].geometry.location.lat;
                let lng = response.data.results[0].geometry.location.lng;


                let marker = new google.maps.Marker({
                    position: {lat: lat, lng: lng},
                    map: myMap,
                    title: nameCity[0]

                });


            }).catch(function (error) {
                console.log(error);
            })
        }
    }
}


let originalOnload = window.onload;
window.onload = function () {
    if (originalOnload) {
        originalOnload();
    }
    $(document).ready(function () {
        ajaxPagination()
    });

    $(document).ajaxStop(function () {
        ajaxPagination()
    });

    $(document).ready(function () {
        ajaxSearch()
    })

};