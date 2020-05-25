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