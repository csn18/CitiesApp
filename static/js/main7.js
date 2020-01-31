import {dropDown, pagination, searchBox, initMap} from "./logic.js";

dropDown();
pagination();
searchBox();
(async () => {
    await initMap([]);
})();
