#  Manual Testing Documentation

##  Create Post Functionality

| Description                     | Steps                                                                 | Expected Outcome                              | Actual Outcome | Status |
|---------------------------------|-----------------------------------------------------------------------|------------------------------------------------|----------------|--------|
| User creates a valid post       | Login → Navigate to Create Post → Fill in form → Submit              | Post is created and appears on homepage        |  Post was created and showed correctly on homepage  | Works      |
| User submits empty form         | Login → Navigate to Create Post → Submit without filling anything    | Error messages appear                          |  no error, but does not post empty              |  Pending      |
| User adds image to post         | Login → Create Post → Upload image → Submit                          | Post displays uploaded image                   |  Image added              | works        |
| User includes a rating in post  | Login → Create Post → Select rating → Submit                         | Rating saved and visible in post detail        |   Rating added and appears in post correctly             | Works       |

##  Commenting on Posts

| Description                     | Steps                                                              | Expected Outcome                                  | Actual Outcome | Status |
|---------------------------------|--------------------------------------------------------------------|---------------------------------------------------|----------------|--------|
| Add a comment as logged-in user | Login → Go to post → Fill comment form → Submit                    | Comment appears below post                        | Comments appears in comment correctly               | Works       |
| Add a comment without rating    | Login → Go to post → Leave rating blank → Submit                   | Comment appears with "No rating provided" message | Comment post with no rating               |  Pending      |
| Submit empty comment            | Login → Go to post → Submit without content                        | Error message shown                               | Message correctly shown             |    Works    |

##  Rating Posts and Comments

| Description                 | Steps                                                       | Expected Outcome                           | Actual Outcome | Status |
|-----------------------------|-------------------------------------------------------------|--------------------------------------------|----------------|--------|
| Add rating to existing post | Login → Go to post → Select rating → Submit                 | Rating added, average updated              | Does not allow to rate withbout comment               |   Works, revise     |
| Rating average calculation  | Rate post + comment → View average rating                   | Correct average shown                      |  Rate, post, view work              | Works       |
| Duplicate rating            | User rates same post twice                                  | Error shown or previous rating updated     |  Allows to doble rate              |  Not Working      |

##  User Authentication

| Description                   | Steps                                                          | Expected Outcome                          | Actual Outcome | Status |
|-------------------------------|----------------------------------------------------------------|-------------------------------------------|----------------|--------|
| New user registration         | Visit site → Click Sign Up → Fill form → Submit                | Account created and user is logged in     | New users can created and stay log               | Work       |
| Login with valid credentials  | Visit Login page → Enter credentials → Submit                  | User is logged in and redirected          | Users are log and redirected to home        |Work        |
| Login with invalid credentials| Visit Login page → Enter invalid info → Submit                 | Error message shown                       | Error message shown when credentials dont mach               | Works       |

##  Admin Features

| Description                    | Steps                                                              | Expected Outcome                              | Actual Outcome | Status |
|--------------------------------|--------------------------------------------------------------------|------------------------------------------------|----------------|--------|
| Admin edits post via dashboard | Login as admin → Admin Panel → Edit post                          | Changes saved and visible on site              | Admin edits shows in site               |Works        |
| Admin deletes a comment        | Login as admin → Admin Panel → Delete comment                     | Comment removed                                | Coments remove by Admin               |Works        |

##  Navigation and Layout

| Description                    | Steps                                                   | Expected Outcome                                | Actual Outcome | Status |
|--------------------------------|---------------------------------------------------------|-------------------------------------------------|----------------|--------|
| Responsive layout test         | Open site on mobile, tablet, desktop                    | Layout adjusts properly for each screen size    | Layout change with the size of the screens               |  Works      |
| Navbar updates after login     | Login as user → Check navbar                            | Links for logout/profile visible                | Navbar uptdates after login               |Work        |
| Navbar before login            | Visit site → View navbar                                | Login/Register links visible                    | Login /Register are visible before login               |Work        |
