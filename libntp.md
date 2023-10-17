
---

## `ntp`

A class for dealing with NTP requests. It also provides methods forformatting dates according to both the MM-DD-YYYY HH:MM:SS and ISO8601
formats. It can deal with local timezones and has no external depenencies.
In the henceforth documentation, MM-DD-YYYY HH:MM:SS will be referred toas 'UTC format'.
Also, P%Y-%m-%dT%H:%M:%S%z will be known as ISO8601.
I am aware there are different variants, this is this project's one.


---
### `ntp.__init__(self, server: str = 'ptbtime1.ptb.de') -> None:`
#### Description

Initialize the object with a 0 value for the Unix TS,and the system time for the date object.


#### Arguments:
`server`: int - NTP server, by default German metrology institute        

---
### `ntp.__currenttz() -> datetime.timedelta:`
#### Description

Internal method that returns the current timezone.This information is user set in the environment variables.
This is mainly for the static easy-use methods.

#### Arguments:
This function has no arguments.

---
### `ntp.__tzstr() -> str:`
#### Description

Internal method that formats the UTC offset as a string.Examples:
+7-8
+0

#### Arguments:
This function has no arguments.

---
### `ntp.iso8601(self, offset: float = 0) -> str:`
#### Description

Return the date_object formatted in ISO8601

#### Arguments:
`offset`: float - UTC offset in hours (can be floating-point)        

---
### `ntp.iso8601r(offset_hour: float = 0) -> str:`
#### Description

Quick access ISO8601 formatted date, offset in hours

#### Arguments:
`offset_hour`: float - UTC offset in hours (can be float)        

---
### `ntp.local_iso8601() -> str:`
#### Description

Quick access ISO8601 formatted date, offset in hours, in local TZ

#### Arguments:
This function has no arguments.

---
### `ntp.local_utc() -> str:`
#### Description

Quick access UTC formatted date, offset in hours, in local TZ

#### Arguments:
This function has no arguments.

---
### `ntp.request(self) -> tuple:`
#### Description

Sets the class variables to the appropriate values, from the ping.From the server specified at object creation.

#### Arguments:
This function has no arguments.

---
### `ntp.request_utcr(offset_hour: float = 0) -> str:`
#### Description

Quick access UTC formatted date

#### Arguments:
`offset_hour`: float - UTC offset in hours (can be float)        

---
### `ntp.utc(self, offset: float = 0) -> str:`
#### Description

Return the date_object property formatted in UTC format.

#### Arguments:
`offset`: float - UTC offset in hours (can be floating-point)        

---