"matching_criteria": {
		"address1": {string},
		"address2": {string},
		"address3": {string},
		"city": {string},
		"country": {string},
		"latitude": {double},
		"longitude": {double},
		"name": {string},
		"phone": {string},
		"postal_code": {string},
		"state": {string},
		"yelp_business_id": {string}
	},
	"options": {
		"create_if_missing": {boolean},
		"use_matching_criteria_for_update": {boolean},
	},
	"partner_business_id": {string},
	"update": {
		"about_this_business_history": {string},
		"about_this_business_specialties": {string},
		"about_this_business_year_established": {string},
		"about_this_business_bio": {string},
		"about_this_business_bio_first_name": {string},
		"about_this_business_bio_last_name": {string},
		"accepts_credit_cards": {boolean},
		"accepts_insurance": {boolean},
		"address1": {string},
		"address2": {string},
		"address3": {string},
		"alcohol": {string},
		"by_appointment_only": {boolean},
		"categories": [
			{string}
		],
		"caters": {boolean},
		"city": {string},
		"closed": {boolean},
		"coat_check": {boolean},
		"comment": {string},
		"contactless_delivery": {boolean},
		"contactless_payment": {boolean},
		"country": {string},
		"covid_19_virus_response": {string},
		"curbside_pickup": {boolean},
		"customers_must_wear_masks": {boolean},
		"delivery": {boolean},
		"desktop_cta": Call to Action – Desktop Object,
		"display_url": {string},
		"dogs_allowed": {boolean},
		"drive_thru": {boolean},
		"employees_wear_gloves": {boolean},
		"employees_wear_masks": {boolean},
		"group_bookings": {boolean},
		"group_name": {string},
		"happy_hour": {boolean},
		"has_tv": {boolean},
		"hours": [
			{
				"day": {string},
				"date": {date},
				"open": {time},
				"close": {time},
				"action": {string}
			}
		],
		"in_store_shopping": {boolean},
		"is_customer": {boolean},
		"is_black_owned": {boolean},
		"is_latinx_owned": {boolean},
		"is_owner_verified": {boolean},
		"latitude": {double},
		"limited_capacity": {boolean},
		"longitude": {double},
		"menu_data": Menu Data Object,
		"menu_url": {string},
		"mobile_cta": Call to Action – Mobile Object,
		"name": {string},
		"parking": {
			"garage": {boolean},
			"lot": {boolean},
			"street": {boolean},
			"valet": {boolean},
			"validated": {boolean}
		},
		"metered_phone": {string},
		"outdoor_seating": {boolean},
		"opening_date": {date},
		"on_premise_access": {boolean},
		"phone": {string},
		"photos": [
			Business Photo Object,
		],
		"platform_service": Platform Service Object,
		"postal_code": {string},
		"provides_santizers_to_customers": {boolean},
		"proof_of_vaccination_required": {boolean},
		"sanitizing_between_customers": {boolean},
		"service_area": [
			{string}
		],
		"service_offerings": Service Offerings Object, 
		"jobs_data": Jobs Data Object (Coming soon),
		"smoking": {string},
		"social_distancing": {boolean},
		"staff_fully_vaccinated": {boolean},
		"state": {string},
		"store_code": {string},
		"take_out": {boolean},
		"takes_reservations": {boolean},
		"temperature_check": {boolean},
		"temporarily_closed": {date},
		"url": {string},
		"waiter_service": {boolean},
		"wheelchair_accessible": {boolean},
		"wifi": {string}

{
  "matching_criteria": {
    "latitude": {double},
    "longitude": {double},
    "name": {string},
    "type": {"yacht" | "car"}, // New field to specify type
    // ... other existing fields ...
  },
  "update": {
    "yacht_details": { // New object for yacht-specific details
      "model": {string},
      "length": {string},
      "builder": {string},
      "year": {string},
      "dock_location": {string}
    },
    "car_details": { // New object for car-specific details
      "make": {string},
      "model": {string},
      "year": {string},
      "color": {string},
      "rental_location": {string}
    },
    "availability": {boolean},
    "pricing": {
      "rental_rate": {number},
      "sale_price": {number}
    },
    "image_gallery": [ // Array of image URLs
      {string} // URL
    ],
    "reviews": [ // Array of review objects
      {
        "user_id": {string},
        "rating": {number},
        "comment": {string},
        "date": {date}
      }
    ],
    // ... other existing fields ...
  }
}
