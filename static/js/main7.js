import {dropDown, pagination, searchBox, initMap, ajaxExec} from "./logic.js";

(async () => {
    await initMap((await ajaxExec('/ajaxFunction'))['cities']);
})();
dropDown();
pagination();
searchBox();

