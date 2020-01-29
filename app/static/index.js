async function getWeatherDetails() {
    const place = document.getElementById('location').value;
    console.log(place)
    const result = await fetch(`http://localhost:5000/location/${place}`, {
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const {data } = await result.json();
    return data;
}
window.addEventListener('load', async () => {
    document.getElementById('location').value = 'Nairobi';
    const data  = await fetchWeather();
    const { formatted_time } = data;
    const day = document.getElementById('day');
    if(day) {
        day.innerHTML = formatted_time
    }
});
function fetchWeather() {
    getWeatherDetails().then(data => {
        document.querySelector('.city').innerHTML = data['city'];
        document.querySelector('.temp').innerHTML = data['temperature'];
        document.getElementById('visibility').innerHTML = data['visibility'];
        document.getElementById('wind').innerHTML = data['wind_speed'];
        document.getElementById('cloud').innerHTML = data['cloud_cover'];
        document.getElementById('humidity').innerHTML = data['humidity'];
        document.getElementById('hourly-summary').innerHTML = data['hourly_summary'];
        document.querySelector('.weather').innerHTML = data['current_summary'];

    })
}