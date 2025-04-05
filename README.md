# notWebobs

Web pages for seismic information.

## Description

Various scripts written for the webobs installation at MVO. Available at http://webobs.mvo.ms:8080/.


## Scripts

| File       | Function |
| -------------| -------------------|
| *check_holdings.pl* | Script to update *holdings_detailed.txt*. |
| *check_holdings.sh* | Script to run *check_holdings.pl* and update *holdings.txt*. Runs once a day as a cronjob.|
| *find_img.pl* | Standalone Perl script to find plot files (only used in debugging).|
| *seismic_monthly_plot_viewer.cgi* | Displays monthly montages of helicorders. Only used in *notWebobs*.|
| *seismic_plot_viewer.cgi* | Main script.|
| *seismic_plot_viewer_mob.cgi* | Temporary version of script for use on mobile devices.|
| *update_mlocate.pl* | Script to update mlocate databases. Runs once a day as a cronjob.|


## Author

Roderick Stewart, Dormant Services Ltd

rod@dormant.org

https://services.dormant.org/

## Version History

* 1.0-dev
    * Working version

## License

This project is licensed to Montserrat Volcano Observatory.
