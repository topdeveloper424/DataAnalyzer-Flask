from flask_assets import Bundle

common_css = Bundle(
    'pages/waves/css/waves.min.css',
    'bower_components/bootstrap/css/bootstrap.min.css',
    'pages/waves/css/waves.min.css',
    'icon/themify-icons/themify-icons.css',
    'icon/font-awesome/css/font-awesome.min.css',
    'css/jquery.mCustomScrollbar.css',
    'pages/chart/radial/css/radial.css',
    'css/style.css',
    filters='cssmin',
    output='public/css/common.css'
)

common_js = Bundle(
    'bower_components/jquery/js/jquery.min.js',
    'bower_components/jquery-ui/js/jquery-ui.min.js',
    'bower_components/popper.js/js/popper.min.js',
    'bower_components/bootstrap/js/bootstrap.min.js',
    'pages/widget/excanvas.js',
    'pages/waves/js/waves.min.js',
    'bower_components/jquery-slimscroll/js/jquery.slimscroll.js',
    'bower_components/modernizr/js/modernizr.js',
    'js/SmoothScroll.js',
    'js/jquery.mCustomScrollbar.concat.min.js',
    'bower_components/chart.js/js/Chart.js',
    filters='jsmin',
    output = 'public/js/common.js'
)

jschart = Bundle(
    'pages/widget/amchart/gauge.min.js',
    'pages/widget/amchart/serial.min.js',
    'pages/widget/amchart/light.min.js',
    'pages/widget/amchart/pie.min.js',
    filters='jsmin',
    output='public/js/chart.js'

)
jslayout = Bundle(
    'js/pcoded.min.js',
    'js/vertical/vertical-layout.min.js',
    'pages/dashboard/custom-dashboard.js',
    'js/script.js',
    filters = 'jsmin',
    output = 'public/js/layout.js'
)

#file page-------------------------------------------------------------------------------

files_css = Bundle(
    'bower_components/bootstrap/css/bootstrap.min.css',
    'pages/waves/css/waves.min.css',
    'icon/themify-icons/themify-icons.css',
    'icon/icofont/css/icofont.css',
    'icon/font-awesome/css/font-awesome.min.css',
    'css/component.css',
    'bower_components/datatables.net-bs4/css/dataTables.bootstrap4.min.css',
    'pages/data-table/css/buttons.dataTables.min.css',
    'bower_components/datatables.net-responsive-bs4/css/responsive.bootstrap4.min.css',
    'css/style.css',
    'css/jquery.mCustomScrollbar.css',
    filters = 'cssmin',
    output = 'public/js/files.css'

)

files_js = Bundle(
    'bower_components/jquery/js/jquery.min.js',
    'bower_components/jquery/js/jquery.min.js',
    'bower_components/popper.js/js/popper.min.js',
    'bower_components/bootstrap/js/bootstrap.min.js',
    'pages/waves/js/waves.min.js',
    'bower_components/jquery-slimscroll/js/jquery.slimscroll.js',
    'bower_components/modernizr/js/modernizr.js',
    'bower_components/modernizr/js/css-scrollbars.js',
    'bower_components/datatables.net/js/jquery.dataTables.min.js',
    'bower_components/datatables.net-buttons/js/dataTables.buttons.min.js',
    'pages/data-table/js/jszip.min.js',
    'pages/data-table/js/pdfmake.min.js',
    'pages/data-table/js/vfs_fonts.js',
    'bower_components/datatables.net-buttons/js/buttons.print.min.js',
    'bower_components/datatables.net-buttons/js/buttons.html5.min.js',
    'bower_components/datatables.net-bs4/js/dataTables.bootstrap4.min.js',
    'bower_components/datatables.net-responsive/js/dataTables.responsive.min.js',
    'bower_components/datatables.net-responsive-bs4/js/responsive.bootstrap4.min.js',
    'pages/data-table/js/data-table-custom.js',
    'js/pcoded.min.js',
    'js/vertical/vertical-layout.min.js',
    'js/jquery.mCustomScrollbar.concat.min.js',
    'js/script.js',
    filters = 'jsmin',
    output = 'public/js/files.js'


)

settings_css = Bundle(
    'bower_components/bootstrap/css/bootstrap.min.css',
    'pages/waves/css/waves.min.css',
    'icon/themify-icons/themify-icons.css',
    'icon/icofont/css/icofont.css',
    'icon/font-awesome/css/font-awesome.min.css',
    'css/component.css',
    'css/style.css',
    'css/jquery.mCustomScrollbar.css',
    filters = 'cssmin',
    output = 'public/js/settings.css'
)

settings_js = Bundle(
    'bower_components/jquery/js/jquery.min.js',
    'bower_components/jquery/js/jquery.min.js',
    'bower_components/popper.js/js/popper.min.js',
    'bower_components/bootstrap/js/bootstrap.min.js',
    'pages/waves/js/waves.min.js',
    'bower_components/jquery-slimscroll/js/jquery.slimscroll.js',
    'bower_components/modernizr/js/modernizr.js',
    'bower_components/modernizr/js/css-scrollbars.js',
    'bower_components/bootstrap-tagsinput/js/bootstrap-tagsinput.js',
    'bower_components/bootstrap-maxlength/js/bootstrap-maxlength.js',
    'js/pcoded.min.js',
    'js/vertical/vertical-layout.min.js',
    'js/jquery.mCustomScrollbar.concat.min.js',
    'js/script.js',
    filters = 'jsmin',
    output = 'public/js/files.js'
)

analyize_css = Bundle(
    'bower_components/bootstrap/css/bootstrap.min.css',
    'pages/waves/css/waves.min.css',
    'icon/themify-icons/themify-icons.css',
    'icon/icofont/css/icofont.css',
    'icon/font-awesome/css/font-awesome.min.css',
    'bower_components/select2/css/select2.min.css',
    'css/component.css',
    'bower_components/datedropper/css/datedropper.min.css',
    'bower_components/datatables.net-bs4/css/dataTables.bootstrap4.min.css',
    'pages/data-table/css/buttons.dataTables.min.css',
    'css/style.css',
    'css/jquery.mCustomScrollbar.css',
    filters = 'cssmin',
    output = 'public/js/analyize.css'
)

analyize_js = Bundle(
    'bower_components/jquery/js/jquery.min.js',
    'bower_components/jquery-ui/js/jquery-ui.min.js',
    'bower_components/popper.js/js/popper.min.js',
    'bower_components/bootstrap/js/bootstrap.min.js',
    'pages/widget/excanvas.js',
    'pages/waves/js/waves.min.js',
    'bower_components/jquery-slimscroll/js/jquery.slimscroll.js',
    'bower_components/modernizr/js/modernizr.js',
    'bower_components/modernizr/js/css-scrollbars.js',
    'bower_components/select2/js/select2.full.min.js',
    'bower_components/multiselect/js/jquery.multi-select.js',
    'js/jquery.quicksearch.js',
    'pages/advance-elements/select2-custom.js',
    'pages/advance-elements/moment-with-locales.min.js',
    'bower_components/datedropper/js/datedropper.min.js',
    'bower_components/datatables.net/js/jquery.dataTables.min.js',
    'bower_components/datatables.net-bs4/js/dataTables.bootstrap4.min.js',
    'js/pcoded.min.js',
    'js/vertical/vertical-layout.min.js',
    'js/jquery.mCustomScrollbar.concat.min.js',
    'js/script.js',
    filters = 'jsmin',
    output = 'public/js/analyize.js'
)