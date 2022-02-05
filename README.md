# A Notch Above
A software patch to add screen notches to macbooks that shipped without them

[As debuted at PyCascades](https://docs.google.com/presentation/d/e/2PACX-1vTdQm_EwHEs2KXMg2KrIwgGOzbpGi5n_0fzD_DJh4zhlzBBnjdfBqyfFRgOFG3OciBwdLFVcH3_IZ0T/pub?start=false&loop=false&delayms=5000)

### Usage
To bring up your notch up, just run the `a-notch-above.py` script
```bash
python a-notch-above.py &
```

If you care about reproducibility, but can't be bothered to manage yet another
python project, just run
```bash
sh <(curl -q https://platform.activestate.com/dl/cli/pdli01/install-latest.sh) -c'state activate ucodery/a-state-above'
```
once to set everything up and then run
```bash
state exec python a-notch-above.py &
```
