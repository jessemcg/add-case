# add-case
App designed to quickly add legal citations to a [concordance file](https://help.libreoffice.org/latest/en-US/text/swriter/01/04120250.html). A concordance file keeps track of words or phrases that the user will later want marked as entries for any type of index. This app is written in Python and has a GTK4 GUI. It only works on linux.   

<img src="screenshot.png" width="450">

## Install
Download add case:

	git clone https://github.com/jessemcg/add-case.git
	
Make sure it is executible:

	chmod +x $HOME/add-case/AddCase.py

Run it from the terminal

	python $HOME/add-case/AddCase.py

Or place the above command in a script launching app like [Launcher](https://extensions.gnome.org/extension/5874/launcher/).

# Usage
To automatically generate a table of authorities after a brief as been written, edit the table of authorities and select the concordance file.

<img src="chose_concordance.png" width="650">
