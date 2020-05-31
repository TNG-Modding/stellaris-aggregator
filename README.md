# stellarisfiles

## Localisation fixes

(:)(?=[0-9]{1}|\s"{1}) with middot
(?<!l_english):{1} with nothing
replace middot with colon
^\s*#.* with nothing
^\s*\n$ with nothing
#.*$ with nothing careful not to delete valid stuff
:[0-9]{1} with :
(?<!:\s)"(?!\n|\s*\n|$) with '


## Parsing event files

There are duplicates of children such as two settings files below:

    create_fleet = {
        settings = {
            spawn_debris = no
        }
        effect = {
            set_owner = PREV
            create_ship_design = {
                design = "NAME_Derelict"
            }
            create_ship = {
                name = "NAME_Salvage"
                design = last_created_design
                upgradable = no
            }
            set_location = FROMFROM
        }
        settings = {
            can_upgrade = no
            can_change_composition = no
            uses_naval_capacity = no
        }
    }

And duplicate events such as :
  
    country_event: {},
    country_event: {}