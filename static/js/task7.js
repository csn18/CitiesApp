'use strict';

let countryId = 1;
let cities = '';
let pageCount = '';
let pageId = '';

function ajaxSearch() {
    $(document).ready(function () {
        $('#searchBox').on('input', function (e) {
            let textInSearchBox = $('#searchBox').val();


            $.ajax({
                url: '/ajaxSearch',
                type: 'GET',
                data: {text: textInSearchBox},
                success: (result) => {
                    countryId = result['countryId'];
                    cities = result['cities'];
                    pageCount = result['pageCount'];

                    initMap();

                    $('#pagination').empty();
                    for (let page = 1; page <= pageCount; page++) {
                        $('#pagination').append(`<li class="page-item"><a class="page-link" href>${page}</a></li>`);

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


function ajaxPagination() {
    $('#pagination a.page-link').each((index, element) => {
        $(element).click((e) => {
            e.preventDefault();

            pageId = index + 1;

            $.ajax({
                url: '/ajaxFunction',
                type: 'GET',
                data: {pageId: pageId, countryId: countryId},
                success: (result) => {
                    pageCount = result['pageCount'];
                    cities = result['cities'];

                        initMap();

                        $('#pagination').empty();
                        for (let page = 1; page <= pageCount; page++) {
                            $('#pagination').append(`<li class="page-item"><a class="page-link" href>${page}</a></li>`);

                        $('#listGroup').empty();
                        for (let city of cities) {
                            $('#listGroup').append(`<li class="list-group-item">${city}</li>`)
                        }
                    }
                }
            })
        })
    })
}


function ajaxDropdown() {
    $('#dropDown a.dropdown-item').each((index, element) => {
        $(element).click((e) => {
            e.preventDefault();

            countryId = index + 1;

            $.ajax({
                url: '/ajaxFunction',
                type: 'GET',
                data: {countryId: countryId},
                success: (result) => {
                    countryId = result['countriesId'];
                    cities = result['cities'];
                    pageCount = result['pageCount'];

                    initMap();

                    $('#pagination').empty();
                    for (let page = 1; page <= pageCount; page++) {
                        $('#pagination').append(`<li class="page-item"><a class="page-link" href>${page}</a></li>`);

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
        center: {lat: 40, lng: 0},
        zoom: 2
    };

    geocode();

    function geocode() {
        let myMap = new google.maps.Map(document.getElementById('map'), opt);
        let apiKey = 'AIzaSyAJSa41jnaiHI4OD54Vg507O0qQKcXeY-0';
        for (let nameCity of cities) {
            axios.get('https://maps.googleapis.com/maps/api/geocode/json', {
                params: {
                    address: nameCity,
                    key: apiKey
                }
            }).then(function (response) {

                let lat = response.data.results[0].geometry.location.lat;
                let lng = response.data.results[0].geometry.location.lng;

                new google.maps.Marker({
                    position: {lat: lat, lng: lng},
                    map: myMap,
                    title: nameCity

                });

            }).catch(function (error) {
                console.log(error);
            })
        }
    }
}


window.onload = function () {

    $(document).ready(function () {
        ajaxPagination()
    });

    $(document).ajaxStop(function () {
        ajaxPagination()
    });

    $(document).ready(function () {
        ajaxSearch()
    });

    $(document).ready(function () {
        ajaxDropdown()
    })

};