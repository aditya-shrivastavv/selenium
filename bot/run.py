from booking.booking import Booking


with Booking() as bot:
    bot.launch_website()
    bot.close_popup()
    # bot.change_currency()
    bot.destination("Mumbai")
    bot.selectDates(checkin="2023-09-08", checkout="2023-09-09")