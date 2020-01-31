export const ajaxExec = (url, data) => {
    return $.ajax({
        url: url,
        type: 'GET',
        data: data
    })
};

export const paginationFill = (pageCount, cities) => {
    $('#pagination').empty();
    for (let page = 1; page <= pageCount; page++) {
        $('#pagination').append(`<li class="page-item"><a class="page-link" href>${page}</a></li>`);
    }

    $('#listGroup').empty();
    for (let city of cities) {
        $('#listGroup').append(`<li class="list-group-item">${city}</li>`)
    }
};

export const initMap = async (cities) => {
    let opt = {
        center: {lat: 40, lng: 0},
        zoom: 2
    };

    let myMap = new google.maps.Map(document.getElementById('map'), opt);
    let apiKey = 'AIzaSyAJSa41jnaiHI4OD54Vg507O0qQKcXeY-0';
    for (let nameCity of cities) {
        const response = await axios.get('https://maps.googleapis.com/maps/api/geocode/json', {
            params: {
                address: nameCity,
                key: apiKey
            }
        });

        let lat = response.data.results[0].geometry.location.lat;
        let lng = response.data.results[0].geometry.location.lng;

        new google.maps.Marker({
            position: {lat: lat, lng: lng},
            map: myMap,
            title: nameCity
        });
    }
};

let countryId = 1;
export const dropDown = () => {
    $("#dropDown").on('click', 'a', async function (e) {
        e.preventDefault();
        countryId = $(this).index() + 1;
        const ajaxFunction = await ajaxExec('/ajaxFunction', {countryId: countryId});
        paginationFill(ajaxFunction['pageCount'], ajaxFunction['cities'])
        if (window.location.pathname === '/task7') await initMap(ajaxFunction['cities']);
    });
};

export const pagination = () => {
    $("#pagination").on('click', 'li', async function (e) {
        e.preventDefault();
        const ajaxFunction = await ajaxExec('/ajaxFunction', {
            countryId: countryId,
            pageId: $(this).index() + 1
        });
        paginationFill(ajaxFunction['pageCount'], ajaxFunction['cities'])
        if (window.location.pathname === '/task7') await initMap(ajaxFunction['cities']);
    });
};

export const searchBox = () => {
    $('#searchBox').on('input', async function (e) {
        e.preventDefault();
        const ajaxFunction = await ajaxExec('/ajaxFunction', {
            text: $('#searchBox').val()
        });
        paginationFill(ajaxFunction['pageCount'], ajaxFunction['cities'])
        countryId = ajaxFunction['countryId'];
        if (window.location.pathname === '/task7') await initMap(ajaxFunction['cities']);
    });
};