This code is for learning the way to use the library "mysql.connector" for python.

I have a Raspberry PI 3 where I have all my databases.

The script called "WebSacraping_NombresApellidos" is the first step that I needed for creating my databases.
I used an API from "DATAMX" where there are many databases with data related with Mexico. I found three databases really usefull. Two of them are databases with the names more commons in Mexico also the frecuency that each name was found in their databases separated by sex. And the other one is the last names more commons and the frecuency depending the place that they are. In Mexico its a law to have 2 last names, (paternal and maternal, in this order) so the last name frecuency changes in order the position.

I got the response of the API and saved the database in the raspberry pi in my local server of MariaDB. I needed to parse the response, because it was a JSON.

Of course, I created a USER in the Raspberry for just QUERY, INSERT and a MASTER User, the DataBase "DatosMexico" and the table "Nombres_H" (Male Names), "Nombres_M" (Female Names) and APELLIDOS (Last names) where I saved dall this information.

In stade of stole a Database of Banks, I created a Fake Employees database called "Usuarios" and Fake Data for each one. Firstly, I created the fake employees that need and ID, the Level in the Organigram that they are right now, their salaries and the date when they started to work in my fake bank.

I used the "random.randomint" function to crate the ID. For creating the Level and Salary I used the function "np.random.choice" from the library "numpy". That function needs a vector with the data, the size that returns and a vector with the probabilities for each data. The bank's structure is the next.
"
# 5% Level 1
# 15% Level 2
# 35% Level 3
# 45% Level 4
"
Acordding with the Level, the salary should be between the next amounts (obviously in MX Currency), and it was made by the function randint.
"
# Level 1  50,0000 - 35,000
# Level 2  40,0000 - 22,000
# Level 3  25,0000 - 18,000
# Level 4  20,0000 - 10,000
"
The date was completely random. The only rule was do not exceed 30 years from now on.

With the Employees database created, I used the class Datos_Usuario_Fake (developed by me ü) to fill the database called Datos_Usuarios. It was created with 5 columns; the ID is PRIMARY KEY and in the same time is FOREING KEY from the Employees Database. The other 4 columns are name, last name, sex and date of birth.

The sex column is a random, the name and last name column was fill by the same way that Level column from "Usuarios" database, with the function "random. choice" using the frequency’s column of names database.

For the date of birth column, it was a bit different. I took the date when started to work in the bank to randomize the date of birth limiting the maximum age to 60 years and keeping in mind that they was be able to start to work in the bank when they have been at least 20 years.

Finally, I practice with that databases creating Query each time more complex and you can see that in the scripts that start with the name "ConsultasMySQL".

...SaaV