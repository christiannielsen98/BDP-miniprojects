# Data
The data is accessible through <a href="https://www.dropbox.com/s/nerfrhbrseev928/CleanML-datasets-2020.zip?dl=0&file_subpath=%2Fdata"> Dropbox</a>, in the directories KDD, KDD_major, KDD_minor, and KDD_uniform. The original data, delimited into separate 6 datasets, donations.csv, essays.csv, projects.csv, resources.csv, outcomes.csv, and sampleSubmission.csv, is available on <a href="https://www.kaggle.com/c/kdd-cup-2014-predicting-excitement-at-donors-choose/data"> Kaggle</a>

For this project, the data from Dropbox was used, and put in the following structure.
| Code

| Data

-- | KDD

---- | dirty_train.csv

---- | raw.csv

-- | KDD_major

---- | mislabel_clean_raw.csv

---- | raw.csv

-- | KDD_minor

---- | mislabel_clean_raw.csv

---- | raw.csv

-- | KDD_uniform

---- | mislabel_clean_raw.csv

---- | raw.csv

| .gitignore

| LICENSE

| REAME.md

# Data Fields
Below is a brief explanation of the provided data fields. Descriptions of self-explanatory names are omitted.

- <b> is_exciting </b> - ground truth of whether a project is exciting from business perspective
- <b> at_least_1_teacher_referred_donor </b> - teacher referred = donor donated because teacher shared a link or publicized their page
- <b> fully_funded </b> - project was successfully completed
- <b> at_least_1_green_donation </b> - a green donation is a donation made with credit card, PayPal, Amazon or check
- <b> great_chat </b> - project has a comment thread with greater than average unique comments
- <b> three_or_more_non_teacher_referred_donors </b> - non-teacher referred is a donor that landed on the site by means other than a teacher referral link/page
- <b> one_non_teacher_referred_donor_giving_100_plus </b> - see above
- <b> donation_from_thoughtful_donor </b> - a curated list of ~15 donors that are power donors and picky choosers (we trust them selecting great projects)
- <b> great_messages_proportion </b> -  how great_chat is calculated. proportion of comments on the project page that are unique. If > avg (currently 62%) then great_chat = True
- <b> teacher_referred_count </b> - number of donors that were teacher referred (see above)
- <b> non_teacher_referred_count </b> - number of donors that were non-teacher referred (see above)
- <b> projectid </b> - project's unique identifier
- <b> teacher_acctid </b> - teacher's unique identifier (teacher that created a project)
- <b> schoolid </b> - school's unique identifier (school where teacher works)
- <b> school_ncesid </b> - public National Center for Ed Statistics id
- <b> school_latitude </b>
- <b> school_longitude </b>
- <b> school_city </b>
- <b> school_state </b>
- <b> school_zip </b>
- <b> school_metro </b>
- <b> school_district </b>
- <b> school_county </b>
- <b> school_charter </b> - whether a public charter school or not (no private schools in the dataset)
- <b> school_magnet </b> - whether a public magnet school or not
- <b> school_year_round </b> - whether a public year round school or not
- <b> school_nlns </b> - whether a public nlns school or not
- <b> school_kipp </b> - whether a public kipp school or not
- <b> school_charter_ready_promise </b> - whether a public ready promise school or not
- <b> teacher_prefix </b> - teacher's gender
- <b> teacher_teach_for_america </b> - Teach for America or not
- <b> teacher_ny_teaching_fellow </b> - New York teaching fellow or not
- <b> primary_focus_subject </b> - main subject for which project materials are intended
- <b> primary_focus_area </b> - main subject area for which project materials are intended
- <b> secondary_focus_subject </b> - secondary subject
- <b> secondary_focus_area </b> - secondary subject area
- <b> resource_type </b> - main type of resources requested by a project
- <b> poverty_level </b> - school's poverty level.
- <b> highest </b>: 65%+ free of reduced lunch
- <b> high </b>: 40-64%
- <b> moderate </b>: 10-39%
- <b> low </b>: 0-9%
- <b> grade_level </b> - grade level for which project materials are intended
- <b> fulfillment_labor_materials </b> - cost of fulfillment
- <b> total_price_excluding_optional_support </b> - project cost excluding optional tip that donors give to DonorsChoose.org while funding a project
- <b> total_price_including_optional_support </b> - see above
- <b> students_reached </b> - number of students impacted by a project (if funded)
- <b> eligible_double_your_impact_match </b> - project was eligible for a 50% off offer by a corporate partner (logo appears on a project, like Starbucks or Disney)
- <b> eligible_almost_home_match </b> - project was eligible for a $100 boost offer by a corporate partner
- <b> date_posted </b> - data a project went live on the site
- <b> donationid </b> - unique donation identifier
- <b> projectid </b> - unique project identifier (project that received the donation)
- <b> donor_acctid </b> - unique donor identifier (donor that made a donation)
- <b> donor_city </b>
- <b> donor_state </b>
- <b> donor_zip </b>
- <b> is_teacher_acct </b> - donor is also a teacher
- <b> donation_timestamp </b>
- <b> donation_to_project </b> - amount to project, excluding optional support (tip)
- <b> donation_optional_support </b> - amount of optional support
- <b> donation_total </b> - donated amount
- <b> dollar_amount </b> - donated amount in US dollars
- <b> donation_included_optional_support </b> - whether optional support (tip) was included for DonorsChoose.org
- <b> payment_method </b> - what card/payment option was used
- <b> payment_included_acct_credit </b> - whether a portion of a donation used account credits redemption
- <b> payment_included_campaign_gift_card </b> - whether a portion of a donation included corporate sponsored giftcard
- <b> payment_included_web_purchased_gift_card </b> - whether a portion of a donation included citizen purchased giftcard (ex: friend buy a giftcard for you)
- <b> payment_was_promo_matched </b> - whether a donation was matched 1-1 with corporate funds
- <b> via_giving_page </b> - donation given via a giving / campaign page (example: Mustaches for Kids)
- <b> for_honoree </b> - donation made for an honoree
- <b> donation_message </b> - donation comment/message. Used to calcualte great_chat
- <b> projectid </b> - unique project identifier
- <b> teacher_acctid </b> - teacher id that created a project
- <b> title </b> - title of the project
- <b> short_description </b> - description of a project
- <b> need_statement </b> - need statement of a project
- <b> essay </b> - complete project essay
- <b> resourceid </b> - unique resource id
- <b> projectid </b> - project id that requested resources for a classroom
- <b> vendorid </b> - vendor id that supplies resources to a project
- <b> vendor_name </b>
- <b> project_resource_type </b> - type of resource
- <b> item_name </b> - resource name (ex: ipad 32 GB)
- <b> item_number </b> - resource item identifier
- <b> item_unit_price </b> - unit price of the resource
- <b> item_quantity </b> - number of a specific item requested by a teacher

# Fields with errors
The following data fields contains errors for the KDD_uniform/raw data

- teacher_teach_for_america
- eligible_double_your_impact_match
- school_charter
- eligible_almost_home_match
- school_nlns
- school_kipp
- school_magnet
- school_charter_ready_promise
- teacher_ny_teaching_fellow
- school_year_round
- is_exciting