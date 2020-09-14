<form method="post" id="booking" action="/booking/">
        <h3>Book an event</h3>
        <table>
            <tbody><tr><th><label for="id_user">User:</label></th><td><select name="user" required="" id="id_user">
  <option value="" selected="">---------</option>

  <option value="1">tek</option>

</select></td></tr>
<tr><th><label for="id_event">Event:</label></th><td><select name="event" required="" id="id_event">
  <option value="" selected="">---------</option>

  <option value="1">sadads:londen</option>

  <option value="2">rwr:erewre</option>

</select></td></tr>
<tr><th><label for="id_session">Session:</label></th><td><select name="session" required="" id="id_session">
  <option value="" selected="">---------</option>

  <option value="1">Morning</option>

  <option value="2">Afternoon</option>

  <option value="3">Evening</option>

  <option value="4">fds</option>

  <option value="5">ef</option>

  <option value="6">ef</option>

</select></td></tr>
<tr><th><label for="id_seats">Seats:</label></th><td><input type="number" name="seats" required="" id="id_seats"></td></tr>
            <tr>
                <td></td>
                <td><input type="submit" class="button" name="booking-form" value="Submit"></td>
            </tr>
        </tbody></table>
        <input type="hidden" name="csrfmiddlewaretoken" value="teclc0mbu5ueX4og5QXnbzJlXHsuEvHqgSceY8vCxDanajGKFLW3kluAn2MpvRFd">
    </form>