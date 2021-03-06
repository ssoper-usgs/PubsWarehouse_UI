

from flask_assets import Environment, Bundle

from . import app

base_metrics_js = Bundle(
    'metrics/js/analyticsData.js',
    'metrics/js/analyticsGraph.js',
    'metrics/js/dataUtils.js',
)
bundles={
    'js_base_libs' : Bundle(
        'pubswh/js/plugins.js',
        filters='rjsmin',
        output='gen/base_libs.js'
    ),
    'js_advanced_search' : Bundle(
        'pubswh/js/searchMap.js',
        'pubswh/js/clearFeatureControl.js',
        'pubswh/js/advancedSearchForm.js',
        'pubswh/js/searchFormOnReady.js',
        filters='rjsmin',
        output='gen/advanced_search.js'
    ),
    'metrics_publications_js' : Bundle(
        base_metrics_js,
        Bundle('metrics/js/pubsGraphController.js'),
        filters='rjsmin',
        output='gen/metrics_publications.js'
    ),
    'metrics_publications_aquisition_js' : Bundle(
        base_metrics_js,
        Bundle('metrics/js/pubsAcquisitionGraphController.js'),
        filters='rjsmin',
        output='gen/metrics_publications_acquisition.js'
    ),
    'metrics_publication_js': Bundle(
        base_metrics_js,
        Bundle('metrics/js/pubGraphController.js'),
        filters='rjsmin',
        output='gen/metrics_publication_js'
    ),

    'usgs_style' : Bundle(
        'manager/less/usgs_header_footer.less',
        filters='less,cssmin',
        output='gen/usgs_style.css'
    ),
    'css_base' : Bundle(
        'pubswh/css/normalize.css',
        'pubswh/css/main.css',
        filters='cssmin',
        output='gen/min_base.css'
    ),
    'auth_style' : Bundle(
        'auth/less/auth.less',
        depends=[
            'manager/less/usgs_header_footer.less'
        ],
        filters='less,cssmin',
        output='gen/auth_style.css'
    ),
    'manager_style' : Bundle(
        'manager/less/manager_custom.less',
        depends=[
            'manager/less/usgs_header_footer.less',
            'manager/less/manage_publications.less',
            'manager/less/publication.less',
            'manager/less/bibliodata.less',
            'manager/less/links.less',
            'manager/less/contributors.less',
            'manager/less/spn.less',
            'manager/less/cataloging.less',
            'manager/less/geospatial.less',
            'manager/less/editSeriesTitle.less',
            'manager/less/manageContributors.less',
            'manager/less/manageAffiliations.less'
        ],
        filters='less,cssmin',
        output='gen/manager_style.css'
    ),
    'metrics_style' : Bundle(
        'metrics/less/metrics_custom.less',
        depends=[
            'manager/less/usgs_header_footer.less',
        ],
        filters='less,cssmin',
        output='gen/metrics_style.css'
    ),
}

assets = Environment(app)
assets.register(bundles)

