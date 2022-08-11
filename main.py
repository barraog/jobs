from lxml import html
import requests
import pickle
import os.path
from collections import Counter

headers= {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

page = requests.get('https://www.irishjobs.ie/ShowResults.aspx?Keywords=python&PerPage=500',
                    headers=headers
)
#print(page.content)
c = """

<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"><![endif]-->
<!--[if IE 9]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!-->
<html class="no-js">
<!--<![endif]-->
<head>

    <meta charset="utf-8">
    <script src="/bundles/js/WebSiteSpeed-js?v=lgVwvWCvPO_CO1rcDmsZrVuBQjaOyiCh5hPpSBUjrKk1"></script>


    <link rel="apple-touch-icon" sizes="175x175" href="/img/logos/apple-touch-icon175x175.png" />
    <meta name="apple-itunes-app" content="app-id=1025737011">
    <meta name="google-play-app" content="app-id=com.saongroup.irishjobs">
    <meta name="viewport" content="width=device-width, maximum-scale=1" id="metaViewport" />
    <meta name="format-detection" content="telephone=no">
    <meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible">
    <meta name="description" content="Looking for Python jobs ? We have 7 for you to choose from with salaries up to 80000. Apply today." />
    <meta name="keywords" content="Python Jobs, irish jobs" />

<meta http-equiv='X-Frame-Options' content='deny'>
    <!-- Use title if it's in the page YAML frontmatter -->
    <title>Python Jobs August 2022 on Irishjobs</title>
    <link href="/bundles/stylesheets/sweetalert-css?v=ltZbih6RlhPFTI8nlZVK3tXTvdyGME11mxmvWd7u35g1" rel="stylesheet"/>

    <link href="/stylesheets/main-styles-css?v=oa6jnp6VQbVayZV-fpNpC6CM7F3CkydwvFJe3VW0UPI1" rel="stylesheet"/>

    <script src="//assets.adobedtm.com/001951d04f0f0e0f889f72b0546583f37849391c/satelliteLib-b454c8535ede363ab59481e4225401adcf41173a.js"></script>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAxwBbp3rTSPXP3IcLzmYo_wK4Bh5zpqgE&amp;libraries=places&amp;language=en-GB"></script>
    <script src="/bundles/js/irish-public-js?v=0SARlrpTxtR1DnoorQY8Cp08YV9C7KqEoWj_Hp6I4jw1"></script>

    <script src="/bundles/js/recommender-logger-js?v=Wt8SH0adtcb45E4u7l6jPM8IpTN3B6S38ANbm4WT4IA1"></script>


    <script src="/bundles/Common/fuploader-js?v=qGpiyuHIEzsyK5-haLzyCURdBmEqtr3KaqM5-IjpzQQ1"></script>

    
<script src="/bundles/js/analytics-insight-js?v=YeYr1Wi6yGdzk3XQq0IgPtEryR1Jx66_o3Zr5G_ILPA1"></script>


    <!-- DataLayer-->

    <script language="javascript">


        var digitalData = { "page__language":"EN",
"page__country":"IE",
"page__category":"searchjobs",
"page__type":"show-result",
"user__visitor_id":"7f6cb0d6fd414e349241cd586bbaa5bb",
"user__login_status":"anonymous",
"user__visit_id":"huzpohmmcpgzkpplktnoeajw",
"listing__is_seo_url":"false",
"listing__sorting":"job-relevant",
"listing__job_ids":"8831442,8830303,8822885,8822335,8820970,8821075,8827953,8828674,8826877,8826748,8816368,8819382,8826415,8819043,8818592,8818625,8819019,8826059,8818623,8817625,8817228,8816637,8824033,8827618,8827617,8820055,8827178,8824642,8816486,8830176,8831402,8824444,8827306,8823308,8827313,8830184,8829318,8821899,8822610,8831121,8820529,8824983,8823618,8823107,8826372,8823631,8828936,8830191,8827499,8827161,8823582,8824452,8830370,8830750,8825472,8830689,8822869,8826256,8830517,8830355,8823535,8829453,8830603,8823495,8826266,8820915,8820766,8821813,8827160,8829297,8828832,8823652,8829212,8830554,8824450,8828709,8822485,8823295,8818337,8822668,8828566,8821640,8823656,8830980,8830580,8826238,8816914,8828270,8821673,8826084,8817762,8817312,8823494,8823492,8818598,8821793,8830977,8826411,8827128,8825043",
"listing__job_count":"285",
"listing__jobs_per_page":"500",
"listing__page_number":"1",
"listing__search_algorithm":"StepMatch-Apollo-Jigsaw",
"listing__is_user_initiated":"false",
"jobsearchfilter__keywords":"python",
"jobsearchfilter__recruiter_type":"employer-agency",
 };

        window.digitalData["user_registration_successful"] = '';
        window.digitalData["user_login_successful"] = '';

        window.digitalData["user__communication_settings_subscribe"] = '';
        window.digitalData["user__communication_settings_unsubscribe"] = '';

    </script>


    <script type="text/javascript">
        function inIframe() {
            try {
                var whiteList = false;
                if (whiteList) {
                    return false;
                }

                return window.self !== window.top;
            } catch (e) {
                return true;
            }
        }

        if (inIframe()) {
            window.location.href = '/noframe.html';
        }

        $(document).ready(function () {
            $('input, textarea').placeholder();
            trackingCommunicationSettings();
        });

        function trackingCommunicationSettings() {
            try {
                if (digitalData.user_registration_successful) {
                    if (digitalData.user__communication_settings_subscribe) {
                        _satellite.setVar('Settings Subscribe', digitalData.user__communication_settings_subscribe);
                        _satellite.track('tracksettingssubscribe');
                    }

                    if (digitalData.user__communication_settings_unsubscribe) {
                        _satellite.setVar('Settings UnSubscribe', digitalData.user__communication_settings_unsubscribe);
                        _satellite.track('tracksettingsunsubscribe');
                    }
                }
            } catch (e) {}
        }


    </script>

    <!--[if lte IE 8]>
       <script src="/bundles/Common/js/bluecube/vendor/modernizr-js?v=Xter60MgPLtKZvN6EHPm89ACEZryCauoJCN04SRQfG01"></script>

    <![endif]-->
    <!-- Fix scaling when rotating an iPhone -->
    <script>var metas = document.getElementsByTagName('meta'); var i; if (navigator.userAgent.match(/iPhone/i)) { for (i = 0; i < metas.length; i++) { if (metas[i].name == "viewport") { metas[i].content = "width=device-width, minimum-scale=1.0, maximum-scale=1.0"; } } document.addEventListener("gesturestart", gestureStart, false); } function gestureStart() { for (i = 0; i < metas.length; i++) { if (metas[i].name == "viewport") { metas[i].content = "width=device-width, minimum-scale=0.25, maximum-scale=1.6"; } } }</script>
    <!-- Typekit -->
    <link href='/Common/js/SmartBanner/password-smartbanner-css?v=oE0xW8_rv_WmatqMouWw6QbvLLzXmSO9ba7skdnq6dQ1' type='text/css' rel='stylesheet' media='screen' />


    
    
        <meta name="robots" content="noindex, nofollow" />

                <script type="text/javascript">
            if (window.Saon == undefined)
                Saon = {};
            if (window.Saon.SSARecommender == undefined)
                window.Saon.SSARecommender = {};

            window.Saon.SSARecommender.UserHashId = "7F6CB0D6-FD41-4E34-9241-CD586BBAA5BB";
            window.Saon.SSARecommender.MyStepStoneId = "7f6cb0d6-fd41-4e34-9241-cd586bbaa5bb";
            window.Saon.SSARecommender.UserIP = "84.203.187.164";
            window.Saon.SSARecommender.EventName = "";
            window.Saon.SSARecommender.OriginId = 3000;
            window.Saon.SSARecommender.Hash = 1593593570;
            window.Saon.SSARecommender.SessionId = "huzpohmmcpgzkpplktnoeajw";
            window.Saon.SSARecommender.ssImageUrl = "https://ssa.stepstone.com/ssa";
            window.Saon.SSARecommender.listingId = 0;
            window.Saon.SSARecommender.algorithm = "StepMatch-Apollo-Jigsaw";
            window.Saon.SSARecommender.TjgOriginId = "301";
            window.Saon.SSARecommender.TjgHash = 1660249612;
            window.Saon.SSARecommender.TjgJsId = "7f6cb0d6-fd41-4e34-9241-cd586bbaa5bb";
            window.Saon.SSARecommender.TjgJobId = 0;

            </script>


    
    <script type="text/javascript">
            if (window.Saon == undefined)
                Saon = {};
            if (window.Saon.SSASearch == undefined)
                window.Saon.SSASearch = {};
            
            window.Saon.SSASearch.SearchType = "freeText";
            window.Saon.SSASearch.WhatSearch = "python";
            window.Saon.SSASearch.WhereSearch = "";
            window.Saon.SSASearch.Orderby = "RelevanceDESC";
            window.Saon.SSASearch.ResultsPerPage = 500;
            window.Saon.SSASearch.NumberOfTotalResults = 285;
            window.Saon.SSASearch.ListingIds = [8831442,8830303,8822885,8822335,8820970,8821075,8827953,8828674,8826877,8826748,8816368,8819382,8826415,8819043,8818592,8818625,8819019,8826059,8818623,8817625,8817228,8816637,8824033,8827618,8827617,8820055,8827178,8824642,8816486,8830176,8831402,8824444,8827306,8823308,8827313,8830184,8829318,8821899,8822610,8831121,8820529,8824983,8823618,8823107,8826372,8823631,8828936,8830191,8827499,8827161,8823582,8824452,8830370,8830750,8825472,8830689,8822869,8826256,8830517,8830355,8823535,8829453,8830603,8823495,8826266,8820915,8820766,8821813,8827160,8829297,8828832,8823652,8829212,8830554,8824450,8828709,8822485,8823295,8818337,8822668,8828566,8821640,8823656,8830980,8830580,8826238,8816914,8828270,8821673,8826084,8817762,8817312,8823494,8823492,8818598,8821793,8830977,8826411,8827128,8825043];
            window.Saon.SSASearch.TjgJobIds = [98382308,98361107,98213849,98200173,98173189,98175025,98321311,98332947,98300564,98297867,98088960,98141435,98279800,98135948,98126415,98127146,98135551,98273347,98127107,98112172,98104982,98093370,98232571,98315327,98315306,98163153,98306611,98245607,98090193,98359334,98381322,98242439,98310055,98220082,98310062,98359449,98344789,98191421,98206019,98375229,98164204,98251901,98225087,98216129,98279635,98225336,98337374,98359513,98312791,98306271,98224032,98242568,98362591,98369045,98262066,98368554,98213374,98277564,98365485,98362414,98223149,98347452,98367387,98222887,98277745,98172787,98169749,98189771,98306273,98344389,98334873,98225773,98342705,98366458,98242535,98333708,98202882,98219643,98123952,98207533,98331149,98187444,98225830,98373299,98366871,98277475,98099744,98325608,98187932,98273541,98163176,98106666,98222879,98222877,98126475,98189207,98373243,98279688,98305459,98253295];
            window.Saon.SSASearch.Page = 1;
            window.Saon.SSASearch.Offset = 0;

            window.Saon.SSASearch.Widgets = {};
                                        window.Saon.SSASearch.Widgets.RecruiterType =[2,1];


            
    </script>

    <script src="/bundles/js/recommender-irish-js?v=hkVt-psWXPKYzF8zj6CJi_ZnOEovJNgcb28Ozb8Bp-o1"></script>



    
    
<link rel="stylesheet" href="/skylight-ui/static/irishjobs.ie.css?_=97ee331" />





    <!-- anti-flicker snippet (recommended)  -->
    <style>
        .async-hide {
            opacity: 0 !important;
        }
    </style>
    <script src="/Common/js/anti-flicker.js?v=1.1"></script>
</head>
<body>

<!-- Google Tag Manager -->
<noscript>
    <iframe src="//www.googletagmanager.com/ns.html?id=GTM-NGWT48"
            height="0" width="0" style="display: none; visibility: hidden"></iframe>
</noscript>
<script>
    (function (w, d, s, l, i) {
        w[l] = w[l] || []; w[l].push(
            { 'gtm.start': new Date().getTime(), event: 'gtm.js' }

        ); var f = d.getElementsByTagName(s)[0],
            j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : ''; j.async = true; j.src =
            '//www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
    })(window, document, 'script', 'dataLayer', 'GTM-NGWT48');
</script>
<!-- End Google Tag Manager -->
    


<script src="https://cdn.jsdelivr.net/npm/vue@2.5.17"></script>
<script src="https://www.irishjobs.ie/vue-components/1.2.0/modal-consent-component.min.js"></script>

<input type="hidden" id="txtObjJson" value="{&quot;yourPrivacyText&quot;:&quot;Your privacy&quot;,&quot;bannerText&quot;:&quot;This site uses cookies and similar technologies to collect and process personal data that recollects your activities and preferences. Some of the personal data, stored on your device, is processed by trusted service providers. We do this to personalise our site, services and the adverts you are shown on and off our website. Click &#39;I accept&#39; to consent to the use of these technologies or &#39;Settings&#39; if you wish to manage your settings. You can always change the setting by going to the &lt;a href=\&quot;/about/cookie-policy\&quot;&gt;Cookie Policy&lt;/a&gt; page. Necessary cookies enable core functionality such as security, network management, and accessibility. You may disable these by changing your browser settings, but this may affect how the website functions.&quot;,&quot;settingsText&quot;:&quot;Settings&quot;,&quot;acceptText&quot;:&quot;I accept&quot;,&quot;acceptAllText&quot;:&quot;Accept All&quot;,&quot;valuePrivacyText&quot;:&quot;We value your privacy&quot;,&quot;modalTitle&quot;:&quot;Here you can control if you want to receive advertising via third-parties.&quot;,&quot;alwaysActiveText&quot;:&quot;Always Active&quot;,&quot;informationStorageTitle&quot;:&quot;Information storage, access and measurement&quot;,&quot;informationStorageText&quot;:&quot;The storage of information, or access to information that is already stored, on your device such as advertising identifiers, device identifiers, cookies, and similar technologies. The collection of information about your use of the content, and combination with previously collected information, used to measure, understand, and report on your usage of the service.&quot;,&quot;informationAdvertsTitle&quot;:&quot;Adverts for other goods and services on this website as well as job adverts on other websites&quot;,&quot;informationAdvertsText&quot;:&quot;This allows us to display career and job related adverts to you while you are on other websites. For example, this allows us to show you the latest suitable jobs whilst you are catching up on the news. It also allows other companies to advertise to you whilst you are on this website.&quot;,&quot;moreInformationPolicyText&quot;:&quot;You can find out more information on the data we collect and what we do with it within our &lt;a href=\&quot;/about/cookie-policy\&quot;&gt;Cookie Policy&lt;/a&gt;.&quot;,&quot;confirmText&quot;:&quot;Confirm&quot;}" />
<input type="hidden" id="domainTxt" value="https://www.irishjobs.ie" />

<span id="app-modal">
    <App :show-banner="false" :id-modal="idModal" ref="mainRef" :text-object="objectText" :cookie-domain="domain" :secure-cookie="true"></App>
</span>

<script>
    var strObj = JSON.parse($('#txtObjJson').val());
    var strDomain = getDomain();
    var app = new Vue({
        el: '#app-modal',
        data: function () {
            return {
                idModal: 'mainModal',
                objectText: strObj,
                domain: strDomain
            }
        }
    });

    //Create a listener for the custom event when the cookie is created
    var appListener = document.querySelector('#app');

    //We add an event listener so we can react to the creation of the cookie
    appListener.addEventListener('cookieCreated',
        function (dataEvent) {
            dataLayer.push({
                'event': 'cookieConsentChanged'
            });
        });

    function getDomain() {
        var domain = $("#domainTxt").val();
        if (domain == null || domain === "" || domain === ".localhost" || domain === "localhost" || domain.includes("localhost"))
            return window.location.hostname;

        return getSiteDomainName(domain) ;
    }
    function getSiteDomainName(url) {
        var match = url.match(/^(?:https?:\/\/)?(?:[^.]+\.)?([^:\/\n\?\=]+)/im);
        if (match != null && match.length > 1 && typeof match[1] === 'string' && match[1].length > 0) {
            return "." + match[1];
        }
        return null; }
</script>



    

        <header id="global-header">
            <nav class="container">
                <ul id="unlogged" class="new-header">
                    <li class="logo mobile-menu">
                        <a href='/' title="IrishJobs.ie" alt="IrishJobs.ie">IrishJobs.ie</a>
                    </li>
                    <li class="saved-jobs .mobile-menu">
                        <a href="/myprofile/saved-jobs" class="opc-mobile saved-jobs__anchor">
                            <div class="icon-start">
                                <i class="fa fa-star"></i>
                                <div class="count-container" style="visibility:hidden">
                                    <span>0</span>
                                </div>

                            </div>
                            <div>
                                <p class="text-transform">saved jobs</p>
                            </div>
                        </a>
                    </li>
                    <li class="profile mobile-menu">
                            <a href='/login' class="opc-mobile">
                                <div class="image-container">
                                    <i class="fa fa-user-circle user-icon"></i>
                                </div>
                                <div>
                                    <p class="text-transform">LOG IN</p>
                                </div>
                            </a>

                        <div id="profile-menu" class="menu-options menu-options__profile">
                                <ul>
                                    <li><a href='/register'><p class="text-transform">Register</p></a></li>
                                    <li>
                                        <a href='/login' id="sign-in-toggle"><p class="text-transform">Log in</p></a>
                                    </li>
                                </ul>
                        </div>
                    </li>
                    <li class="menu mobile-menu">
                        

<nav>
    <div class="opc-mobile" onclick="showHideMenu('main');">
        <div>
            <i class="fa fa-bars"></i>
        </div>
        <div>
            <p class="text-transform">MENU</p>
        </div>
    </div>
    <div id="main-menu" class="menu-options menu-options__main">
        <ul>
            <li class="filter"><a href='https://www.irishjobs.ie/company-reviews'><p class="text-transform">Company Reviews</p></a></li>
        <li id="browse-dropdown" class="filter">
            <a href='/browse-all' class="active dropdown-title-mobile"><p class="text-transform">Browse</p></a>
            <span id="browse-dropdown-title" class="active dropdown-title-desktop"><p class="text-transform">Browse</p></span>
            <div class="dropdown-nav">
                <div class="inner-wrapper-dropdown">
                    <div class="browse-all">
                        <a href='/browse-all'><p class="text-transform">Browse all jobs</p></a>
                    </div>
                    <div class="inner-wrapper-dropdown two-colums">
                        <div class="left">
                            <h3>Popular Categories</h3>
                            <ul>
                                    <li><a href='/Jobs/IT/'>IT </a></li>
                                    <li><a href='/Jobs/Accountancy-Finance/'>Accountancy &amp; Finance </a></li>
                                    <li><a href='/Jobs/Engineering-Utilities/'>Engineering &amp; Utilities </a></li>
                                    <li><a href='/Jobs/Banking-Financial-services-Insurance/'>Banking, Financial services &amp; Insurance </a></li>
                                    <li><a href='/Jobs/Medical-Professionals-Healthcare/'>Medical Professionals &amp; Healthcare </a></li>

                                <li class="view-all"><a href='/job-categories'>View All Categories</a></li>
                            </ul>
                        </div>
                        <div class="right">
                            <h3>Useful links</h3>
                            <ul>
                                <li><a href='/companies'>Employers A-Z</a></li>
                                <li><a href='/agencies'>Agencies A-Z</a></li>

                                <li><a href='/company-reviews'>Company Reviews</a></li>

                                <li><a href='/Jobs/Executive'>Executive Positions</a></li>
                                <li><a href='/Jobs/Graduate'>Graduate Opportunities</a></li>
                                <li><a href='/ShowResults.aspx?rbet=32'>Contract Roles</a></li>
                                <li class="view-all"><a href='/employment-types'>View All Useful links</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

        </li>
        <li id="carrer-dropdown" class="filter">
            <a id="carrer-dropdown-title" href='https://www.irishjobs.ie/careeradvice/' class=" dropdown-title-mobile"><p class="text-transform">Career Advice</p></a>
            <span id="carrer-dropdown-title" class=" dropdown-title-desktop"><p class="text-transform">Career Advice</p></span>
            <div class="dropdown-nav">
                <div class="inner-wrapper-dropdown">
                    <div class="left">
                        <ul>
                            <li><a href='https://www.irishjobs.ie/careeradvice/'>Career Advice </a></li>
                            <li><a href='https://www.irishjobs.ie/careeradvice/job-news/'>Job News</a></li>
                            <li><a href='https://www.irishjobs.ie/careeradvice/cv-advice/'>CV Advice</a></li>
                            <li><a href='https://www.irishjobs.ie/careeradvice/cv-templates/'>CV Templates</a></li>
                            <li><a href='https://www.irishjobs.ie/careeradvice/interview-advice/'>Interview Advice</a></li>
                            <li><a href='https://www.irishjobs.ie/careeradvice/salaries/'>Salaries</a></li>
                            <li><a href='https://www.irishjobs.ie/careeradvice/job-hunting/'>Job Hunting Tips</a></li>
                            <li><a href='https://www.irishjobs.ie/careeradvice/irishjobs-ie-user-guides/'>Help Guides</a></li>
                            <li><a href='https://www.irishjobs.ie/careeradvice/job-descriptions/'>Job Descriptions</a></li>
                            <li><a href='https://www.irishjobs.ie/careeradvice/newsroom/'>Newsroom</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </li>
        <li class="filter  ">
            <a href='/recruiters/' class="ad-job-link "><p class="text-transform">Advertise a Job</p></a>
        </li>
        </ul>
    </div>
</nav>

<script type="text/javascript">
    var carrerDropdownIsOpen = false
    var contextMenuActive = ""
    function handlerOpenDropdowns() {
        if ($(window).width() > 766) {
            $("#main-menu li > span, #main-menu li > a, #username-opc-dropdown > span").click(function () {
                let contextMenu = $(this).next("div")
                if (contextMenuActive == contextMenu.context.id) {
                    $(".active-context-menu").toggle()
                    $(".active-context-menu").removeClass("active-context-menu")
                    contextMenuActive = ""
                    carrerDropdownIsOpen = false
                } else {
                    $(".active-context-menu").toggle()
                    $(".active-context-menu").removeClass("active-context-menu")
                    contextMenu.addClass("active-context-menu")
                    contextMenu.toggle()
                    contextMenuActive = contextMenu.context.id
                    carrerDropdownIsOpen = true
                }
            });

            $(document).click(function (event) {
                var $target = $(event.target);
                if (!$target.closest("#main-menu li > span, #main-menu li > a").length && !$target.closest('.inner-wrapper-dropdown').length) {
                    if (!$target.closest('#username-opc-dropdown > span').length && !$target.closest('.profile-options').length) {
                        if (carrerDropdownIsOpen) {
                            $('.active-context-menu').toggle();
                            $(".active-context-menu").removeClass("active-context-menu")
                            carrerDropdownIsOpen = false
                            contextMenuActive = ""
                        }
                    }
                }
            });
        }

    }

    handlerOpenDropdowns()
</script>

                    </li>

                </ul>
                
            </nav>
        </header>
    
<div id="page">
    <div id="searched-for">
        <div class="container">
            
<script type="text/javascript">
    var IJ_ie8 = false;
</script>

<div id="cancelBtn" class="cancel-show-search-form">Cancel</div>
<form action="/ShowResults.aspx" id="search-job" method="get">        <label class="searched-for-heading"></label>
    <div class="search-job-group-search-form clearable">
        <i class="fa fa-search"></i>
        <input Class="search-job-title search-box" id="Keywords" name="Keywords" placeholder="Job title, skill or company" populated="python" type="text" value="python" />
        <span id="loading"></span>
        <input id="autosuggestEndpoint" name="autosuggestEndpoint" type="hidden" value="/autosuggest" />
        <span class="clearable__clear">&times;</span>
    </div>
    <div class="toggle-form-elements">
        <select Class="search-job-select" id="Location" name="Location"><option value="">Where?</option>
<option selected="selected" value="0">All Locations</option>
<option value="102">Dublin</option>
<option selected="selected" value="0">------------</option>
<option value="21">Antrim</option>
<option value="22">Armagh</option>
<option value="23">Belfast</option>
<option value="2">Carlow</option>
<option value="24">Cavan</option>
<option value="41">Clare</option>
<option value="42">Cork</option>
<option value="25">Derry</option>
<option value="26">Donegal</option>
<option value="27">Down</option>
<option value="102">Dublin</option>
<option value="28">Fermanagh</option>
<option value="61">Galway</option>
<option value="44">Kerry</option>
<option value="3">Kildare</option>
<option value="4">Kilkenny</option>
<option value="5">Laois</option>
<option value="63">Leitrim</option>
<option value="45">Limerick</option>
<option value="6">Longford</option>
<option value="7">Louth</option>
<option value="64">Mayo</option>
<option value="8">Meath</option>
<option value="29">Monaghan</option>
<option value="9">Offaly</option>
<option value="65">Roscommon</option>
<option value="66">Sligo</option>
<option value="47">Tipperary</option>
<option value="30">Tyrone</option>
<option value="48">Waterford</option>
<option value="10">Westmeath</option>
<option value="11">Wexford</option>
<option value="12">Wicklow</option>
<option selected="selected" value="0">[-- General Search --]</option>
<option selected="selected" value="0">All Locations</option>
<option value="87">International</option>
<option value="82">Nationwide</option>
<option value="106">Working from Home</option>
<option value="67">Connacht</option>
<option value="13">Leinster</option>
<option value="101">Midlands</option>
<option value="49">Munster</option>
<option value="31">Ulster</option>
</select>
        <select Class="search-job-select" id="Category" name="Category"><option value="">In All Categories</option>
<option value="8">Accountancy &amp; Finance</option>
<option value="20">Banking, Financial services &amp; Insurance</option>
<option value="11">Beauty, Hair Care, Leisure &amp; Sport</option>
<option value="9">Construction, Architecture &amp; Property</option>
<option value="23">Customer Service, Call Centres &amp; Languages</option>
<option value="13">Education, Childcare &amp; Training</option>
<option value="6">Engineering &amp; Utilities</option>
<option value="2">Environmental, Health &amp; Safety</option>
<option value="27">Executive</option>
<option value="28">Graduate</option>
<option value="1">Hotel &amp; Catering</option>
<option value="16">HR &amp; Recruitment</option>
<option value="3">IT</option>
<option value="4">Legal</option>
<option value="21">Marketing</option>
<option value="17">Medical Professionals &amp; Healthcare</option>
<option value="7">Production, Manufacturing &amp; Materials</option>
<option value="115">Public Sector</option>
<option value="25">Publishing, Media &amp; Creative Arts</option>
<option value="10">Retailing, Wholesaling &amp; Purchasing</option>
<option value="24">Sales</option>
<option value="26">Science, Pharmaceutical &amp; Food</option>
<option value="114">Secretarial &amp; Admin</option>
<option value="14">Security, Trades &amp; General Services</option>
<option value="12">Social &amp; Not for Profit</option>
<option value="5">Telecoms</option>
<option value="19">Tourism, Travel &amp; Airlines</option>
<option value="18">Transport, Warehousing &amp; Motor</option>
</select>
        <div class="checkbox-wrap">
            <input type="checkbox" name="Recruiter" id="employer" checked='checked' value='Company' />
            <label for="employer">Employer</label>
            <input type="checkbox" name="Recruiter" id="agency" checked='checked' value='Agency' />
            <label for="agency">Agency</label>
        </div>
        <div class="inputcontainer">
            <input type="submit" value="Search" class="search-job-btn" id="btnSubmit" name="btnSubmit" />
            <div class="loader-container">
                <i class="loader"></i>
            </div>
        </div>
    </div>
</form><script src="/bundles/js/autosuggest-js?v=8FDnvJ1pA3Bv6YR4TLEi3aDodpalDgCjjpQ-HkOVVGA1"></script>

<script src="/bundles/js/search-form-js?v=gBUutE9f1Hz7vlFNS5aqt0TUNvr_K-zVpUJZb-tZWX81"></script>


        </div>
    </div>

    

<style type="text/css">
    .job-result-title a:visited {
        color: #676767;
    }

        .job-result-title a:visited > strong {
            color: #676767;
        }

    .job-result-title a {
        color: #323232;
        text-decoration: none;
    }
</style>

<script src="/bundles/Common/js/show-results-js?v=OmeKq6sSH8E2IsN_ef83fHSRN_5YlnV_J7ixtwkwXyA1"></script>

<script type="text/javascript">
    if(!saon.Api.AjaxWS) saon.Api.AjaxWS = {};
    saon.Api.AjaxWS.AddRemoveJob =  '/WebService/AjaxWS.asmx/AddRemoveJob';
    saon.Api.AjaxWS.AddExcludedJob =  '/WebService/AjaxWS.asmx/AddExcludedJob';
    saon.Api.AjaxWS.RemoveExcludedJob =  '/WebService/AjaxWS.asmx/RemoveExcludedJob';
    saon.Api.AjaxWS.UpdatePromotedJobNotForMeStatistics =  '/WebService/AjaxWS.asmx/UpdatePromotedJobNotForMeStatistics';
    saon.Api.AjaxWS.UpdatePromotedJobClicksStatistics = '/WebService/AjaxWS.asmx/UpdatePromotedJobClicksStatistics';
    saon.Api.AjaxWS.PromotedStats = '/promoted-stats';

    saon.SiteCookiesApprovedCookieName = 'CONSENTMGR';
    saon.IsUserLoggedIn = 'False'.toLowerCase() === 'true';
    saon.NotForMeJobsCookieNameGuest = 'cajij_g';
    saon.NotForMeJobsCookieNameLogged = 'cajij_l';
    saon.LoggedGuid = '00000000-0000-0000-0000-000000000000';
    saon.GuestGuid = 'aef7b545-7fa1-42e5-9881-276fbbfa37b2';

    if(!saon.Resources.SearchResults) saon.Resources.SearchResults = {};
    saon.Resources.SearchResults.JobSaved = 'Job saved';
    saon.Resources.SearchResults.SaveThisJob = 'Save This Job';
    saon.Resources.SearchResults.PromotedJob = 'Promoted Job';
    saon.Resources.SearchResults.NotForMe = 'Not for me';

    saon.Resources.SearchResults.SavedJobBackgroundColor = '#becd2f';
    saon.Resources.SearchResults.SavedJobColor = '#ffffff';
    saon.Resources.SearchResults.SavedJobStar = '/img/icons/star-white-small.png';

    saon.Resources.SearchResults.SaveThisJobBackgroundColor = '#ffffff';
    saon.Resources.SearchResults.SaveThisJobColor = '#cad466';
    saon.Resources.SearchResults.SaveThisJobStar = '/img/icons/star-green-small.png';

    $(document).ready(function () {
        $("#addjobalertdiv").hide();
        $("#create-job-alert-btn").unbind("click");
        $('#create-job-alert-btn').on('click', function (event) {
            event.stopPropagation();
            $('#addjobalertdiv').slideToggle('fast');
            $('.email-me-jobs-btn').toggleClass('open');
            $('#Email').focus();
        });

    });
</script>
    <div class="container">




            <br />
            <div id="jobalertfeedbackdesktop">
            </div>

        <div id="header-job-result" class="column-wrap order-one-two" style="clear:both;">
                <h1 class="show-results">Python Jobs</h1>

            <div class="serp-breadcrumb">


                    <div id="jobalertfeedbackmobile">
                        <a id="create-job-alert-btn" class="apply-now email-me-jobs-btn job-alert-sp">
                            <span class="envelope">&nbsp</span>Email&nbsp;me&nbsp;jobs&nbsp;like&nbsp;this
                        </a>
                    </div>
            </div>
        </div>

        <div class="column-wrap order-one-two" style="clear:both;">
            <div class="one-third">

                
<script src="/bundles/Common/js/refinements-js?v=nga34lzVN_IQAanPNo_e_RCMF9EhBCJ0i35grtJMLOw1"></script>

<script src="/bundles/js/bsnAutosuggest2-js?v=iHBs42Pso3rJ9j2MkCIGu01hI1QE2b-3aeClx26Ols81"></script>

<link rel='stylesheet' href='/bundles/css/autosuggest-theme?v=gK4_pcAzc8ROzfjcluehIqrTvVcn3DZv4ZqC6K5wpY41' type='text/css' media='screen' charset='utf-8' />


<script type="text/javascript">
    
    var url = '/WebService/AjaxWS.asmx/GetRefineByKeywordJobTitleList';
    if (!saon.Api.AjaxWS)
        saon.Api.AjaxWS = {};
    saon.Api.AjaxWS.GetRefineByKeyword = url;
</script>
<div id="JobSearchRefinements">
    <div class="module refine-search">
        <h2 class="module-heading heading-dark mobile-ref-heading">
            Filter By
        </h2>
        <div class="module-content mobile-refinement">
                    <div class="refine-option">
                        <h4>
                            <div class=ref-recruiter></div>Recruiter Type
                        </h4>
                        <div class="refine-option-toggle">

                            <ul>
                                    <li class=" ">
                                            <a class="job-title" rel="nofollow" href="/python-Jobs?Recruiter=Agency" style="cursor: pointer;">Agency</a>

                                    </li>
                                    <li class=" ">
                                            <a class="job-title" rel="nofollow" href="/python-Jobs?Recruiter=Company" style="cursor: pointer;">Employer</a>

                                    </li>
                            </ul>

                        </div>
                    </div>
                    <div class="refine-hr"></div>
                    <div class="pipes">
                        <span></span>
                    </div>
                    <div class="refine-option">
                        <h4>
                            <div class=ref-location></div>Locations
                        </h4>
                        <div class="refine-option-toggle">

                            <ul>
                                    <li class=" ">
                                            <a class="job-title"  href="/python-Jobs-in-Laois" style="cursor: pointer;">Laois</a>

                                    </li>
                                    <li class=" ">
                                            <a class="job-title"  href="/python-Jobs-in-Longford" style="cursor: pointer;">Longford</a>

                                    </li>
                                    <li class=" ">
                                            <a class="job-title"  href="/python-Jobs-in-Offaly" style="cursor: pointer;">Offaly</a>

                                    </li>
                                    <li class=" ">
                                            <a class="job-title"  href="/python-Jobs-in-Westmeath" style="cursor: pointer;">Westmeath</a>

                                    </li>
                                    <li class=" ">
                                            <a class="job-title"  href="/python-Jobs-in-Carlow" style="cursor: pointer;">Carlow</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title"  href="/python-Jobs-in-Dublin" style="cursor: pointer;">Dublin</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title"  href="/python-Jobs-in-Kildare" style="cursor: pointer;">Kildare</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title"  href="/python-Jobs-in-Kilkenny" style="cursor: pointer;">Kilkenny</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title"  href="/python-Jobs-in-Leinster" style="cursor: pointer;">Leinster</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title"  href="/python-Jobs-in-Louth" style="cursor: pointer;">Louth</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title"  href="/python-Jobs-in-Meath" style="cursor: pointer;">Meath</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title"  href="/python-Jobs-in-Wexford" style="cursor: pointer;">Wexford</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title"  href="/python-Jobs-in-Wicklow" style="cursor: pointer;">Wicklow</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title" rel='nofollow' href="/python-Jobs-in-Dublin-City-Centre" style="cursor: pointer;">Dublin City Centre</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title" rel='nofollow' href="/python-Jobs-in-Dublin-North" style="cursor: pointer;">Dublin North</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title" rel='nofollow' href="/python-Jobs-in-Dublin-South" style="cursor: pointer;">Dublin South</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title" rel='nofollow' href="/python-Jobs-in-Dublin-West" style="cursor: pointer;">Dublin West</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title"  href="/python-Jobs-in-Working-from-Home" style="cursor: pointer;">Working from Home</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title"  href="/python-Jobs-in-Tipperary" style="cursor: pointer;">Tipperary</a>

                                    </li>
                                    <li class=" hidden">
                                            <a class="job-title"  href="/python-Jobs-in-Clare" style="cursor: pointer;">Clare</a>

                                    </li>
                            </ul>

                                <div class="more-options">
                                    <span>show more <span class="guillemet"></span></span>
                                </div>
                        </div>
                    </div>
                    <div class="refine-hr"></div>
                    <div class="pipes">
                        <span></span>
                    </div>
            

                <div class="pipes">
                    <span></span>
                </div>
                <div class="microsite-mobile refine-option">
                    <div class="refine-option">
                        <h4>
                            <div class="ref-jobtype"></div>Job Types
                        </h4>

                        <div class="refine-option-toggle">

                                <ul>
                                    <h4 class="mobile-ref-heading">Python Job Types</h4>
                                        <li class="">
                                            <a href="/Python-Developer-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Python Developer
                                            </a>
                                        </li>
                                        <li class="">
                                            <a href="/Junior-Python-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Junior Python
                                            </a>
                                        </li>
                                        <li class="">
                                            <a href="/Python-Engineer-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Python Engineer
                                            </a>
                                        </li>
                                </ul>
                                                            <h4 class="mobile-ref-heading">Python Related Jobs</h4>
                                <ul>
                                        <li class="">
                                            <a href="/Software-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Software
                                            </a>
                                        </li>
                                        <li class="">
                                            <a href="/Big-Data-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Big Data
                                            </a>
                                        </li>
                                        <li class="">
                                            <a href="/Data-Engineer-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Data Engineer
                                            </a>
                                        </li>
                                        <li class="">
                                            <a href="/Graduate-Software-Engineer-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Graduate Software Engineer
                                            </a>
                                        </li>
                                        <li class="">
                                            <a href="/Software-Programmer-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Software Programmer
                                            </a>
                                        </li>
                                        <li class="">
                                            <a href="/Cloud-Engineer-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Cloud Engineer
                                            </a>
                                        </li>
                                        <li class="">
                                            <a href="/Junior-Software-Engineer-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Junior Software Engineer
                                            </a>
                                        </li>
                                        <li class="">
                                            <a href="/Work-From-Home-Java-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Work From Home Java
                                            </a>
                                        </li>
                                        <li class="">
                                            <a href="/Senior-Systems-Engineer-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Senior Systems Engineer
                                            </a>
                                        </li>
                                        <li class="">
                                            <a href="/Software-Development-Engineer-Jobs"
                                               class="job-title" info="" style="cursor: pointer;">
                                                Software Development Engineer
                                            </a>
                                        </li>
                                </ul>


                        </div>
                    </div>
                    <div class="refine-hr"></div>
                    <br />
                </div>
            <!------------End mobile microsites----------------------->
        </div>
    </div>

        <div class="module refine-search microsites">
            <h2 class="module-heading heading-dark mobile-ref-heading">
                Show Results For
            </h2>
            <div class="module-content">
                    <div class="refine-option">
                        <h4>Python Job Types</h4>
                        <div class="refine-option-toggle">
                            <ul>
                                    <li class="">
                                        <a href="/Python-Developer-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Python Developer
                                        </a>
                                    </li>
                                    <li class="">
                                        <a href="/Junior-Python-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Junior Python
                                        </a>
                                    </li>
                                    <li class="">
                                        <a href="/Python-Engineer-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Python Engineer
                                        </a>
                                    </li>
                            </ul>
                        </div>
                    </div>
                    <div class="refine-hr"></div>

                    <div class="refine-option">
                        <h4>Python Related Jobs</h4>
                        <div class="refine-option-toggle">
                            <ul>
                                    <li class="">
                                        <a href="/Software-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Software
                                        </a>
                                    </li>
                                    <li class="">
                                        <a href="/Big-Data-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Big Data
                                        </a>
                                    </li>
                                    <li class="">
                                        <a href="/Data-Engineer-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Data Engineer
                                        </a>
                                    </li>
                                    <li class="">
                                        <a href="/Graduate-Software-Engineer-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Graduate Software Engineer
                                        </a>
                                    </li>
                                    <li class="">
                                        <a href="/Software-Programmer-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Software Programmer
                                        </a>
                                    </li>
                                    <li class="">
                                        <a href="/Cloud-Engineer-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Cloud Engineer
                                        </a>
                                    </li>
                                    <li class="">
                                        <a href="/Junior-Software-Engineer-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Junior Software Engineer
                                        </a>
                                    </li>
                                    <li class="">
                                        <a href="/Work-From-Home-Java-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Work From Home Java
                                        </a>
                                    </li>
                                    <li class="">
                                        <a href="/Senior-Systems-Engineer-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Senior Systems Engineer
                                        </a>
                                    </li>
                                    <li class="">
                                        <a href="/Software-Development-Engineer-Jobs"
                                           class="job-title" info="" style="cursor: pointer;">
                                            Software Development Engineer
                                        </a>
                                    </li>
                            </ul>
                        </div>
                    </div>
                    <div class="refine-hr"></div>
                                <br />
            </div>
        </div>
    <!------------End microsite--------------->
</div>
                <div class="ad-space">
                    
<!-- Revive Adserver Hosted edition - Ad Management Asynchronous JS Tag - Generated with Revive Adserver v4.2.1 -->
<ins data-revive-zoneid="1568" data-revive-id="727bec5e09208690b050ccfc6a45d384"></ins>
<script async src="//servedby.revive-adserver.net/asyncjs.php"></script>

                </div>
            </div>
            <div class="two-thirds">

                <div class="clear"></div>

                <div class="add-job-alert-container">
                    


<script src="/bundles/Common/js/smartRegistration-js?v=gClZdNojeH1ToDvTKTxtV1tyU_cpPSU71l1g13UACNo1"></script>

<script type="text/javascript">
    saon.Api.AjaxWS.ValidateEmailDomain = '/validate-cv-domain';

    function createJobAlert() {
        var email = "";
        //TO DO: Unify JS code of new job alerts partial views
                
                email = $("#Email").val();
                


        if (email != "") {
            if (validateEmailDomain(email)) {
                $.ajax({
                    type : 'POST',
                    data: { jobAlertName: "python Jobs", email: email, requestURL: "https://www.irishjobs.ie/ShowResults.aspx?Keywords=python&PerPage=500" },
                    dataType: 'json',
                    url: "/CreateJobAlert",
                    success: function (data) {
                        const isMobileScreen = window.isMobileScreen();
                        const jobAlertFeedback = isMobileScreen ? $("#jobalertfeedbackmobile") : $("#jobalertfeedbackdesktop");
                        if (!isMobileScreen) $('#jobalertfeedback').html("");
                        if (data.Success) {
                            var message = "";

                            if (data.NewJobSeeker) {
                                message += "<p class='confirm'><svg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 21 21' style='width: 19px;vertical-align: bottom;enable-background:new 0 0 21 21;' xml:space='preserve'><style type='text/css'>.st0{fill:none;}.st1{fill:#31C104;}</style><g><path class='st0' d='M10.5,20C5.3,20,1,15.7,1,10.5C1,5.3,5.3,1,10.5,1c5.2,0,9.5,4.2,9.5,9.5C20,15.7,15.7,20,10.5,20z'></path><path class='st1' d='M10.5,2c4.7,0,8.5,3.8,8.5,8.5S15.2,19,10.5,19S2,15.2,2,10.5S5.8,2,10.5,2 M10.5,0C4.7,0,0,4.7,0,10.5S4.7,21,10.5,21S21,16.3,21,10.5S16.3,0,10.5,0L10.5,0z'></path></g><g><path class='st0' d='M8.7,14.8c0,0-0.1,0-0.2,0l-3-3c-0.1-0.1-0.1-0.1-0.1-0.2s0-0.1,0.1-0.2c0.1-0.1,0.1-0.1,0.2-0.1c0,0,0.1,0,0.2,0.1l2.8,2.8l6.5-6.5c0.1-0.1,0.1-0.1,0.2-0.1s0.1,0,0.2,0.1c0.1,0.1,0.1,0.1,0.1,0.2c0,0,0,0.1-0.1,0.2l-6.7,6.7C8.8,14.8,8.8,14.8,8.7,14.8z'></path><path class='st1' d='M15.4,6.6c-0.3,0-0.6,0.1-0.9,0.4l-5.8,5.8l-2.1-2.1c-0.2-0.2-0.6-0.4-0.9-0.4c-0.3,0-0.6,0.1-0.9,0.4c-0.5,0.5-0.5,1.3,0,1.8l2.9,2.9c0,0,0,0,0,0c0.2,0.2,0.6,0.4,0.9,0.4s0.6-0.1,0.9-0.4l6.7-6.7c0.5-0.5,0.5-1.3,0-1.8C16.1,6.7,15.7,6.6,15.4,6.6L15.4,6.6z'></path></g></svg>&nbsp; Your job alert email has been created.<br>"
                                message += "An email has been sent to " + email + ".<br>";
                                message += "Please click the link in the email to create your account and start receiving your Job Alerts emails.<br>";
                                message += "The link will expire in 24 hours.</p>"
                            } else {
                                message += "<p class='confirm'><svg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 21 21' style='width: 19px;vertical-align: bottom;enable-background:new 0 0 21 21;' xml:space='preserve'><style type='text/css'>.st0{fill:none;}.st1{fill:#31C104;}</style><g><path class='st0' d='M10.5,20C5.3,20,1,15.7,1,10.5C1,5.3,5.3,1,10.5,1c5.2,0,9.5,4.2,9.5,9.5C20,15.7,15.7,20,10.5,20z'></path><path class='st1' d='M10.5,2c4.7,0,8.5,3.8,8.5,8.5S15.2,19,10.5,19S2,15.2,2,10.5S5.8,2,10.5,2 M10.5,0C4.7,0,0,4.7,0,10.5S4.7,21,10.5,21S21,16.3,21,10.5S16.3,0,10.5,0L10.5,0z'></path></g><g><path class='st0' d='M8.7,14.8c0,0-0.1,0-0.2,0l-3-3c-0.1-0.1-0.1-0.1-0.1-0.2s0-0.1,0.1-0.2c0.1-0.1,0.1-0.1,0.2-0.1c0,0,0.1,0,0.2,0.1l2.8,2.8l6.5-6.5c0.1-0.1,0.1-0.1,0.2-0.1s0.1,0,0.2,0.1c0.1,0.1,0.1,0.1,0.1,0.2c0,0,0,0.1-0.1,0.2l-6.7,6.7C8.8,14.8,8.8,14.8,8.7,14.8z'></path><path class='st1' d='M15.4,6.6c-0.3,0-0.6,0.1-0.9,0.4l-5.8,5.8l-2.1-2.1c-0.2-0.2-0.6-0.4-0.9-0.4c-0.3,0-0.6,0.1-0.9,0.4c-0.5,0.5-0.5,1.3,0,1.8l2.9,2.9c0,0,0,0,0,0c0.2,0.2,0.6,0.4,0.9,0.4s0.6-0.1,0.9-0.4l6.7-6.7c0.5-0.5,0.5-1.3,0-1.8C16.1,6.7,15.7,6.6,15.4,6.6L15.4,6.6z'></path></g></svg>&nbsp; Your job alert email has been created.</p>"
                            }

                            //DTM direct call for jaсreated condition
                            if (data.JaId > 0) {
                                window.digitalData["jobalert__id"] = data.JaId;
                                try {
                                    _satellite.track("jacreated");
                                } catch (e) {}
                            }

                            $("#addjobalertdiv").hide();
                            jobAlertFeedback.html("");
                            jobAlertFeedback.html(message);
                        } else {
                            if (data.JobSeekerRTBFRequestInProgress) {
                                $("#addjobalertdiv").hide();
                                jobAlertFeedback.html("");
                                jobAlertFeedback.html("<p class='error error-ajad'>" + data.Message + "</p>");
                            } else {
                                 $("#addjobalertdiv").hide();
                                 jobAlertFeedback.html("");
                                jobAlertFeedback.html("<p class='error'><?xml version='1.0' encoding='utf-8'?><!-- Generator: Adobe Illustrator 20.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  --><svg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 21 21' style='enable-background:new 0 0 21 21;' xml:space='preserve'><style type='text/css'>.st0{fill:none;}.st1{fill:#E83232;}</style><g><path class='st0' d='M10.5,20C5.3,20,1,15.7,1,10.5C1,5.3,5.3,1,10.5,1c5.2,0,9.5,4.2,9.5,9.5C20,15.7,15.7,20,10.5,20z' /><path class='st1' d='M10.5,2c4.7,0,8.5,3.8,8.5,8.5S15.2,19,10.5,19S2,15.2,2,10.5S5.8,2,10.5,2 M10.5,0C4.7,0,0,4.7,0,10.5S4.7,21,10.5,21S21,16.3,21,10.5S16.3,0,10.5,0L10.5,0z' /></g><g><path class='st1' d='M12.4,14.9C11.1,16.4,9.7,17,9.1,17c-0.5,0-0.9-0.4-0.6-1.9l1.1-4.8c0.1-0.5,0.1-0.6,0-0.6c-0.2,0-0.8,0.4-1.1,0.7L8.2,9.9c1.3-1.3,2.7-2.1,3.4-2.1c0.6,0,0.7,0.7,0.4,2l-1.1,4.7c-0.1,0.6-0.1,0.7,0.1,0.7c0.2,0,0.6-0.3,1.1-0.7L12.4,14.9z M12.8,5.1c0,0.8-0.6,1.5-1.4,1.5c-0.6,0-1-0.5-1-1.1c0-0.8,0.5-1.5,1.4-1.5C12.4,4,12.8,4.5,12.8,5.1z' /></g></svg>&nbsp; You have reached your limit of 10 job alert emails.<br>To save a new job alert email you must delete at least 1 previously <a href='/myprofile/jobalerts'>saved job alert</a>.</p>");
                            }
                        }
                    },
                });
                $("#createjobalert").css("visibility", "hidden");
                $("#addjobalertdiv").append("<img src='/img/icons/AjaxLoader.gif' />");
            } else {
                $("#jobalerterror-msgEmail").css("display", "inline-block");
                $('.name-alert').click(function(){
                    $('#jobalerterror-msgEmail').hide();
                });
            }
        } else {
            $("#jobalerterror-msg").css("display", "inline-block");
            $('.name-alert').click(function(){
                $('#jobalerterror-msg').hide();
            });
        }
    }
</script>

<div id="addjobalertdiv">
    <h4>python Jobs</h4>
    <div class="email-address">
            <input class="name-alert" id="Email" maxlength="255" name="Email-inline" placeholder="EMAIL" type="text" value="">
    </div>
    <div id="jobalerterror-msg">
        <span style="left: -26px; top:-30px; display:block;" class="error-excla field-validation-valid"></span>
        <p>Please enter your email address</p>
    </div>
    <div id="jobalerterror-msgEmail">
        <span style="left: -26px; top:-30px; display:block;" class="error-excla field-validation-valid"></span>
        <p>Please enter a valid email address</p>
    </div>
    <input id="createjobalert" type="button" value="Email me jobs" onclick="createJobAlert();" class="create-alert" />
</div>
                </div>

                <div class="job-options sort-job">
                    <div class="sort-by-wrap">
                            <label class="jobsFound" style="margin-right:30px;">Total Jobs Found: 285</label>
                        <label class="sort-by">Sort By</label>
                        <select class="styled-select" id="SortedBy">
                            <option value="MostRecent" >Most Recent</option>
                            <option value="Relevance" selected=selected>Relevance</option>
                        </select>
                    </div>
                    <ul class="show-count">
                        <li>Show</li>
                            <li><a rel="nofollow"  href="https://www.irishjobs.ie/ShowResults.aspx?Keywords=python&amp;PerPage=25">25</a></li>
                            <li><a rel="nofollow"  href="https://www.irishjobs.ie/ShowResults.aspx?Keywords=python&amp;PerPage=50">50</a></li>
                            <li><a rel="nofollow"  href="https://www.irishjobs.ie/ShowResults.aspx?Keywords=python&amp;PerPage=100">100</a></li>
                        <li>Per Page</li>
                    </ul>
                </div>



                <div id="JobSearchRefinementsMobile"></div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8831442" href='/Jobs/Python-Developer-8831442.aspx' >Python Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€96,000 - €108,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Role: <strong>Python</strong> Developer - My client are a well-established company who are currently looking for a <strong>Python</strong> Developer on a contract basis who is passionate about their work and can thrive in a collaborative environment. * 5+ Years <strong>Python</strong> experience</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8831442">Save This Job </a>
                                    <a class="show-more" jobId="8831442" href='/Jobs/Python-Developer-8831442.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/EOLAS-IT-RECRUITMENT-SPECIALISTS-JOBS-824.aspx"><img alt="EOLAS – IT RECRUITMENT SPECIALISTS JOBS" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/824-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=8cb4c635d6adead42df2b9eb84b077f1b28778e73937bea1752c10c51daa30cc"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830303" href='/Jobs/Senior-Python-Developer-8830303.aspx' >Senior Python Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/EOLAS-IT-RECRUITMENT-SPECIALISTS-JOBS-824.aspx">EOLAS – IT RECRUITMENT SPECIALISTS JOBS</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€65.00 - €80.00 per hour</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span><strong>Python</strong> Developer – 12 month Contract My Dublin City Centre based client is looking for a Senior <strong>Python</strong> Developer on a contract basis for 12 months. <strong>Python</strong> Developer – 12 month Contract - My Dublin City Centre based client is looking for a Senior <strong>Python</strong> Developer on a contract basis for 12 months.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830303">Save This Job </a>
                                    <a class="show-more" jobId="8830303" href='/Jobs/Senior-Python-Developer-8830303.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Morgan-McKinley-5478.aspx"><img alt="Morgan McKinley" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5478-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=e041799ef517bddfea9d49a50299f8ef2f92f64045e019956309b5c225581f9f"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8822885" href='/Jobs/Senior-Python-Developer-8822885.aspx' >Senior Python Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Morgan-McKinley-5478.aspx">Morgan McKinley</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 07/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Strong working knowledge of technologies such as <strong>Python,</strong> Docker and SQL. <strong>Python</strong> SQL REST Docker Kubernetes Ansible Terraform - Requirements: Minimum of 5 years professional experience. Excellent - Minimum of 5 years professional experience. Excellent inter-personal and collaboration skills. Capable of travelling into the Dublin office 1/2 a week.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8822885">Save This Job </a>
                                    <a class="show-more" jobId="8822885" href='/Jobs/Senior-Python-Developer-8822885.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/KPMG-2230.aspx"><img alt="KPMG" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/2230-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=70b910b097a977da48d486929265e361dc253ce15c847f0ad6fc136c225fb414"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8822335" href='/Jobs/Python-Developer-8822335.aspx' >Python Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/KPMG-2230.aspx">KPMG</a>
                                            </h3>
                                        
  <style data-styled="fLtnCS" data-styled-version="4.4.0">
/* sc-component-id: Star__StyledSvg-sc-1ge1c9k-0 */
.sky-component .fLtnCS{margin:0 1px;width:21px;height:21px;}</style>

  

  <div id="sky-65aace24e2b188e9-0" class="sky-component ZG9udXQ"><div><div class="sky-search-rating"><div class="sky-search-rating__stars"><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0z14medhw7jg" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0z14medhw7jg)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient014u489apab1" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient014u489apab1)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0rt5ov1q2ned" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0rt5ov1q2ned)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient000dyq76bcj6a" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="65%" style="stop-color:#f3d756"></stop><stop offset="65%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient000dyq76bcj6a)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0yi4nw6k9ewd" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:#f3d756"></stop><stop offset="0%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0yi4nw6k9ewd)" stroke="#f3d756"></path></svg></div><div class="sky-search-rating__reviews-count">71<!-- --> company<!-- --> <!-- -->reviews</div></div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-0",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"2230","data":{"localId":"2230","surveysCount":71,"overallRatingAvg":3.62646,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 05/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Are you a experienced and motivated PHP / Laravel & <strong>Python</strong> * Are you a experienced and motivated PHP / Laravel & <strong>Python</strong> developer looking for a interesting role where you can learn lots more * Proven experience (5+ Years) as a PHP / <strong>Python</strong> developer - Description & Requirements Do you have a background in building web applications? Description & Requirements</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8822335">Save This Job </a>
                                    <a class="show-more" jobId="8822335" href='/Jobs/Python-Developer-8822335.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Studio-Intelligence-13840.aspx"><img alt="Studio Intelligence" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/13840-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=31fd69766443e3d129abebc79c6fbeca23e61021262131ebfdc62681b12e0eb4"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8820970" href='/Jobs/API-Developer-Python-Net-8820970.aspx' >API Developer - Python / .Net</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Studio-Intelligence-13840.aspx">Studio Intelligence</a>
                                            </h3>
                                        
                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 04/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>API <strong>Python</strong> / .Net Developer, Partial Remote Working Role: Studio Intelligence are looking to recruit a developer with experience in <strong>Python,</strong> .Net or - API <strong>Python</strong> / .Net Developer, Partial Remote Working - Studio Intelligence are looking to recruit a developer with experience in <strong>Python,</strong> .Net or similar, ideally with experience in Azure / AWS.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8820970">Save This Job </a>
                                    <a class="show-more" jobId="8820970" href='/Jobs/API-Developer-Python-Net-8820970.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                                <div class="add-job-alert-container module">
                                    <div class="module-content">
                                        

<script src="/bundles/Common/js/smartRegistration-js?v=gClZdNojeH1ToDvTKTxtV1tyU_cpPSU71l1g13UACNo1"></script>


<script type="text/javascript">
    saon.Api.AjaxWS.ValidateEmailDomain = '/validate-cv-domain';

    function createJobAlertInline() {

        var email = "";
        //TO DO: Unify JS code of new job alerts partial views
                
                    email = $("#Email-inline").val();
                


        $("#jobalerterror-inline").css("display", "none");
        $("#jobalerterror-inlineEmail").css("display", "none");

        if (email != "") {
            if (validateEmailDomain(email)) {
                $("#createjobalert-inline").css("visibility", "hidden");
                $("#jobalertfeedback-inline").append("<img src='/img/icons/AjaxLoader.gif' />");

                $.ajax({
                    type : 'POST',
                    data: { jobAlertName: "python Jobs", email: email, requestURL: "https://www.irishjobs.ie/ShowResults.aspx?Keywords=python&PerPage=500" },
                    dataType: 'json',
                    url: "/CreateJobAlert",
                    success: function (data) {
                        if (data.Success) {
                            var message = "";

                            if (data.NewJobSeeker) {
                                message += "<p class='confirm'><svg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 21 21' style='width: 19px;vertical-align: bottom;enable-background:new 0 0 21 21;' xml:space='preserve'><style type='text/css'>.st0{fill:none;}.st1{fill:#31C104;}</style><g><path class='st0' d='M10.5,20C5.3,20,1,15.7,1,10.5C1,5.3,5.3,1,10.5,1c5.2,0,9.5,4.2,9.5,9.5C20,15.7,15.7,20,10.5,20z'></path><path class='st1' d='M10.5,2c4.7,0,8.5,3.8,8.5,8.5S15.2,19,10.5,19S2,15.2,2,10.5S5.8,2,10.5,2 M10.5,0C4.7,0,0,4.7,0,10.5S4.7,21,10.5,21S21,16.3,21,10.5S16.3,0,10.5,0L10.5,0z'></path></g><g><path class='st0' d='M8.7,14.8c0,0-0.1,0-0.2,0l-3-3c-0.1-0.1-0.1-0.1-0.1-0.2s0-0.1,0.1-0.2c0.1-0.1,0.1-0.1,0.2-0.1c0,0,0.1,0,0.2,0.1l2.8,2.8l6.5-6.5c0.1-0.1,0.1-0.1,0.2-0.1s0.1,0,0.2,0.1c0.1,0.1,0.1,0.1,0.1,0.2c0,0,0,0.1-0.1,0.2l-6.7,6.7C8.8,14.8,8.8,14.8,8.7,14.8z'></path><path class='st1' d='M15.4,6.6c-0.3,0-0.6,0.1-0.9,0.4l-5.8,5.8l-2.1-2.1c-0.2-0.2-0.6-0.4-0.9-0.4c-0.3,0-0.6,0.1-0.9,0.4c-0.5,0.5-0.5,1.3,0,1.8l2.9,2.9c0,0,0,0,0,0c0.2,0.2,0.6,0.4,0.9,0.4s0.6-0.1,0.9-0.4l6.7-6.7c0.5-0.5,0.5-1.3,0-1.8C16.1,6.7,15.7,6.6,15.4,6.6L15.4,6.6z'></path></g></svg>&nbsp; Your job alert email has been created.<br>"
                                message += "An email has been sent to " + email + ".<br>";
                                message += "Please click the link in the email to create your account and start receiving your Job Alerts emails.<br>";
                                message += "The link will expire in 24 hours.</p>"
                            } else {
                                message += "<p class='confirm'><svg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 21 21' style='width: 19px;vertical-align: bottom;enable-background:new 0 0 21 21;' xml:space='preserve'><style type='text/css'>.st0{fill:none;}.st1{fill:#31C104;}</style><g><path class='st0' d='M10.5,20C5.3,20,1,15.7,1,10.5C1,5.3,5.3,1,10.5,1c5.2,0,9.5,4.2,9.5,9.5C20,15.7,15.7,20,10.5,20z'></path><path class='st1' d='M10.5,2c4.7,0,8.5,3.8,8.5,8.5S15.2,19,10.5,19S2,15.2,2,10.5S5.8,2,10.5,2 M10.5,0C4.7,0,0,4.7,0,10.5S4.7,21,10.5,21S21,16.3,21,10.5S16.3,0,10.5,0L10.5,0z'></path></g><g><path class='st0' d='M8.7,14.8c0,0-0.1,0-0.2,0l-3-3c-0.1-0.1-0.1-0.1-0.1-0.2s0-0.1,0.1-0.2c0.1-0.1,0.1-0.1,0.2-0.1c0,0,0.1,0,0.2,0.1l2.8,2.8l6.5-6.5c0.1-0.1,0.1-0.1,0.2-0.1s0.1,0,0.2,0.1c0.1,0.1,0.1,0.1,0.1,0.2c0,0,0,0.1-0.1,0.2l-6.7,6.7C8.8,14.8,8.8,14.8,8.7,14.8z'></path><path class='st1' d='M15.4,6.6c-0.3,0-0.6,0.1-0.9,0.4l-5.8,5.8l-2.1-2.1c-0.2-0.2-0.6-0.4-0.9-0.4c-0.3,0-0.6,0.1-0.9,0.4c-0.5,0.5-0.5,1.3,0,1.8l2.9,2.9c0,0,0,0,0,0c0.2,0.2,0.6,0.4,0.9,0.4s0.6-0.1,0.9-0.4l6.7-6.7c0.5-0.5,0.5-1.3,0-1.8C16.1,6.7,15.7,6.6,15.4,6.6L15.4,6.6z'></path></g></svg>&nbsp; Your job alert email has been created.</p>"
                            }

                            //DTM direct call for jaсreated condition
                            if (data.JaId > 0) {
                                window.digitalData["jobalert__id"] = data.JaId;
                                try {
                                    _satellite.track("jacreated");
                                } catch (e) {}
                            }

                            $("#jobalertfeedback-inline").html("");
                            $("#jobalertfeedback-inline").html(message);
                        } else if (data.JobSeekerRTBFRequestInProgress) {
                            $("#jobalertfeedback-inline").html("");
                            $("#jobalertfeedback-inline").html("<p class='error'>" + data.Message + "</p>");
                        } else {
                            $("#jobalertfeedback-inline").html("");
                            $("#jobalertfeedback-inline").html("<p class='error'><?xml version='1.0' encoding='utf-8'?><!-- Generator: Adobe Illustrator 20.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  --><svg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 21 21' style='enable-background:new 0 0 21 21;' xml:space='preserve'><style type='text/css'>.st0{fill:none;}.st1{fill:#FF9595;}</style><g><path class='st0' d='M10.5,20C5.3,20,1,15.7,1,10.5C1,5.3,5.3,1,10.5,1c5.2,0,9.5,4.2,9.5,9.5C20,15.7,15.7,20,10.5,20z' /><path class='st1' d='M10.5,2c4.7,0,8.5,3.8,8.5,8.5S15.2,19,10.5,19S2,15.2,2,10.5S5.8,2,10.5,2 M10.5,0C4.7,0,0,4.7,0,10.5S4.7,21,10.5,21S21,16.3,21,10.5S16.3,0,10.5,0L10.5,0z' /></g><g><path class='st1' d='M12.4,14.9C11.1,16.4,9.7,17,9.1,17c-0.5,0-0.9-0.4-0.6-1.9l1.1-4.8c0.1-0.5,0.1-0.6,0-0.6c-0.2,0-0.8,0.4-1.1,0.7L8.2,9.9c1.3-1.3,2.7-2.1,3.4-2.1c0.6,0,0.7,0.7,0.4,2l-1.1,4.7c-0.1,0.6-0.1,0.7,0.1,0.7c0.2,0,0.6-0.3,1.1-0.7L12.4,14.9z M12.8,5.1c0,0.8-0.6,1.5-1.4,1.5c-0.6,0-1-0.5-1-1.1c0-0.8,0.5-1.5,1.4-1.5C12.4,4,12.8,4.5,12.8,5.1z' /></g></svg>&nbsp; You have reached your limit of 10 job alert emails.<br>To save a new job alert email you must delete at least 1 previously <a href='/myprofile/jobalerts'>saved job alert</a>.</p>");
                        }
                    },
                });
            } else {
                $("#jobalerterror-inlineEmail").css("display","inline-block");
            }
        } else {
            $("#jobalerterror-inline").css("display","inline-block");
        }
    }
</script>

<div id="addjobalertinlinediv">
    <h4><span>Send me Job Alert emails with jobs matching:</span> python Jobs</h4>
    <div id="jobalertfeedback-inline" class="form-cell clearfix ">
            <input class="name-alert" id="Email-inline" maxlength="255" name="Email-inline" placeholder="example@domain.com" type="text" value="">
                    <input id="createjobalert-inline" type="button" value="Create alert" onclick="createJobAlertInline();" class="create-alert lo" />

    </div>
    <div id="jobalerterror-inline" class="inline">
        <span style="left: -26px; top:-30px; display:block;" class="error-excla field-validation-valid"></span>
        <p>Please enter a valid email address</p>
    </div>
    <div id="jobalerterror-inlineEmail" class="inline">
        <span style="left: -26px; top:-30px; display:block;" class="error-excla field-validation-valid"></span>
        <p>Please enter a valid email address</p>
    </div>
</div>
                                    </div>
                                </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8821075" href='/Jobs/Backend-Python-Developers-8821075.aspx' >Backend Python Developers</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€60,000 - €70,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 04/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span><strong>Python</strong> | Backend | <strong>Python</strong> | Django | Flask - I am working with a world-leading fintech company who are looking for multiple backend <strong>Python</strong> developers to join their growing team. You will be working in a <strong>Python</strong> environment but other language experience can be considered. * Strong coding skills and good knowledge of <strong>Python</strong> <strong>Python</strong> Backend Django Flask AWS Dublin</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8821075">Save This Job </a>
                                    <a class="show-more" jobId="8821075" href='/Jobs/Backend-Python-Developers-8821075.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8827953" href='/Jobs/Python-Developer-8827953.aspx' >Python Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€80,000 - €90,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 03/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span><strong>Python</strong> | Scraping | Scripting |SQL - My client are a unique start-up in the sports trading industry who are looking for a <strong>Python</strong> Developer with strong scripting skills. They are looking for a mid-senior level developer so you need to have a least 3+ years of industry <strong>Python</strong> experience. * 3+ years <strong>Python</strong> experience</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8827953">Save This Job </a>
                                    <a class="show-more" jobId="8827953" href='/Jobs/Python-Developer-8827953.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/EOLAS-IT-RECRUITMENT-SPECIALISTS-JOBS-824.aspx"><img alt="EOLAS – IT RECRUITMENT SPECIALISTS JOBS" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/824-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=8cb4c635d6adead42df2b9eb84b077f1b28778e73937bea1752c10c51daa30cc"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8828674" href='/Jobs/Software-Developer-Java-CSharp-Net-8828674.aspx' >Software Developer (Java, C# / .Net or Python)</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/EOLAS-IT-RECRUITMENT-SPECIALISTS-JOBS-824.aspx">EOLAS – IT RECRUITMENT SPECIALISTS JOBS</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 04/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>My Dublin based client is recruiting for a Software Developer (Java, C# / .Net or <strong>Python</strong>)to join the team on a perm basis, this will on a hybrid model. Due to expansion and growth were currently recruiting for an experienced Software Developers on both frontend and backend technologies in Java, C# / .Net or <strong>Python</strong> .</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8828674">Save This Job </a>
                                    <a class="show-more" jobId="8828674" href='/Jobs/Software-Developer-Java-CSharp-Net-8828674.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Berkley-Recruitment-Group-2330.aspx"><img alt="Berkley Recruitment Group" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/2330-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=97eec2be052b1d01ac7a32f2add4fc5b28901736e56cc3aa0e75125a73636486"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8826877" href='/Jobs/Python-Developer-8826877.aspx' >Python Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Berkley-Recruitment-Group-2330.aspx">Berkley Recruitment Group</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 02/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Cork/">Cork</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>My client, a cutting-edge software company based in Cork are looking to hire a <strong>Python</strong> Developer on a permanent basis. * Strong proficiency and at least 5 years experience in software development ideally developing SaaS solutions in <strong>Python</strong> or Java. <strong>Python</strong> Django Flask - Cork/Remote</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8826877">Save This Job </a>
                                    <a class="show-more" jobId="8826877" href='/Jobs/Python-Developer-8826877.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Berkley-Recruitment-Group-2330.aspx"><img alt="Berkley Recruitment Group" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/2330-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=97eec2be052b1d01ac7a32f2add4fc5b28901736e56cc3aa0e75125a73636486"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8826748" href='/Jobs/Python-Developer-8826748.aspx' >Python Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Berkley-Recruitment-Group-2330.aspx">Berkley Recruitment Group</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 02/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Senior <strong>Python</strong> Developer Dublin Initial 6 month (Long term potential) Fantastic opportunity for a Aenior <strong>Python</strong> to join a large financial services - Senior <strong>Python</strong> Developer - Fantastic opportunity for a Aenior <strong>Python</strong> to join a large financial services company based in Dublin. * Proven programming ability in <strong>Python,</strong> with OO programming & design patterns</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8826748">Save This Job </a>
                                    <a class="show-more" jobId="8826748" href='/Jobs/Python-Developer-8826748.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/JP-Morgan-2201.aspx"><img alt="JP Morgan" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/2201-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=34f341c4f7fdca37f9da1903b0bb8ae7da2d98068a09913915a90ef64e6401d9"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8816368" href='/Jobs/Software-Engineering-Python-8816368.aspx' >Software Engineering - Python</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/JP-Morgan-2201.aspx">JP Morgan</a>
                                            </h3>
                                        
  <style data-styled="fLtnCS" data-styled-version="4.4.0">
/* sc-component-id: Star__StyledSvg-sc-1ge1c9k-0 */
.sky-component .fLtnCS{margin:0 1px;width:21px;height:21px;}</style>

  

  <div id="sky-65aace24e2b188e9-2" class="sky-component ZG9udXQ"><div><div class="sky-search-rating"><div class="sky-search-rating__stars"><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0yvhm57gbsc" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0yvhm57gbsc)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0x1h2wkp4ji" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0x1h2wkp4ji)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0pzzpamqkqeq" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0pzzpamqkqeq)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0s3m4tms3zoi" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="65%" style="stop-color:#f3d756"></stop><stop offset="65%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0s3m4tms3zoi)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0x41wdfod2r" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:#f3d756"></stop><stop offset="0%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0x41wdfod2r)" stroke="#f3d756"></path></svg></div><div class="sky-search-rating__reviews-count">20<!-- --> company<!-- --> <!-- -->reviews</div></div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-2",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"2201","data":{"localId":"2201","surveysCount":20,"overallRatingAvg":3.75699,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Job Description As a member of our Software Engineering Group, we look first and foremost for people who are passionate around solving business</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8816368">Save This Job </a>
                                    <a class="show-more" jobId="8816368" href='/Jobs/Software-Engineering-Python-8816368.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Stelfox-1626.aspx"><img alt="Stelfox" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1626-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=fca5c0061a2933f5e18cd12757f055bf8c9efbd2d158f007ab14c7c09dc4ee6b"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8819382" href='/Jobs/Full-Stack-Python-Engineers-Remote-8819382.aspx' >Full Stack Python Engineers - Remote in Europe</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Stelfox-1626.aspx">Stelfox</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€65,000 - €85,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 31/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Full Stack <strong>Python</strong> Engineers x 20 - Remote in Europe Our exclusive new client is a global cloud-based platform that is redefining visual presentations - Full Stack <strong>Python</strong> Engineers x 20 - Remote in Europe - Here you will be working as a Full Stack Engineer mainly with <strong>Python,</strong> Django, TypeScript, Kubernetes, and a little bit of Scala.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8819382">Save This Job </a>
                                    <a class="show-more" jobId="8819382" href='/Jobs/Full-Stack-Python-Engineers-Remote-8819382.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Morgan-McKinley-5478.aspx"><img alt="Morgan McKinley" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5478-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=e041799ef517bddfea9d49a50299f8ef2f92f64045e019956309b5c225581f9f"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8826415" href='/Jobs/Senior-Python-Engineer-8826415.aspx' >Senior Python Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Morgan-McKinley-5478.aspx">Morgan McKinley</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€90,000 - €120,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 30/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Job Title: Senior <strong>Python</strong> Engineer Industry: Financial Services Location: Dublin Work Policy: 2/3 days a month in the office What you will do: Bring - Job Title: Senior <strong>Python</strong> Engineer * Expertise with core technologies such as <strong>Python.</strong> <strong>Python</strong> SQL REST Open API. Industry: Financial Services - Location: Dublin - Work Policy: 2/3 days a month in the office</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8826415">Save This Job </a>
                                    <a class="show-more" jobId="8826415" href='/Jobs/Senior-Python-Engineer-8826415.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8819043" href='/Jobs/Python-Developer-8819043.aspx' >Python Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€80,000 - €90,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 30/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>They are currently looking for a <strong>Python</strong> Developer to join their team on a permanent, full-time basis. <strong>Python</strong> experience is a must. * <strong>Python</strong> experience (3+years) If you are interested in this role, or would like to discuss one of our other <strong>python</strong> roles on offer, please contact Aimee Thompson at Reperio Human Capital.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8819043">Save This Job </a>
                                    <a class="show-more" jobId="8819043" href='/Jobs/Python-Developer-8819043.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Stelfox-1626.aspx"><img alt="Stelfox" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1626-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=fca5c0061a2933f5e18cd12757f055bf8c9efbd2d158f007ab14c7c09dc4ee6b"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8818592" href='/Jobs/Senior-Python-Developer-8818592.aspx' >Senior Python Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Stelfox-1626.aspx">Stelfox</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 30/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>They are looking to expand their technology operation and hire a Senior <strong>Python</strong> developer for an exciting project. * Proven programming ability in <strong>Python,</strong> with OO programming & design patterns <strong>Python</strong> Developer Django - My client is a leading Financial services organisation with a significant technology presence in Dublin.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8818592">Save This Job </a>
                                    <a class="show-more" jobId="8818592" href='/Jobs/Senior-Python-Developer-8818592.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Stelfox-1626.aspx"><img alt="Stelfox" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1626-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=fca5c0061a2933f5e18cd12757f055bf8c9efbd2d158f007ab14c7c09dc4ee6b"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8818625" href='/Jobs/Python-Engineers-Remote-in-Ireland-8818625.aspx' >Python Engineers - Remote in Ireland</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Stelfox-1626.aspx">Stelfox</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€60,000 - €90,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 30/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span><strong>Python</strong> Engineers required - All Levels!! Here you'll have the opportunity to work on greenfield projects and collaborate with other developers using <strong>Python</strong> & AWS * Solid commercial knowledge of <strong>Python</strong> programming - Our client is a leading provider of information on the financial health of public and private companies</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8818625">Save This Job </a>
                                    <a class="show-more" jobId="8818625" href='/Jobs/Python-Engineers-Remote-in-Ireland-8818625.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Computer-Futures-723.aspx"><img alt="Computer Futures" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/723-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=96907b5237086550249a3c81a9891a0237196a4f735c510a462b2606604c8a67"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8819019" href='/Jobs/Python-Developer-8819019.aspx' >Python Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Computer-Futures-723.aspx">Computer Futures</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 30/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>They are in the early stages of their development but such is the response to their initial range of customer solutions that they are growing quickly and have an immediate need to recruit a <strong>Python</strong> Developer to work alongside their Solution Architect and Product Development Team. Experience of delivering solutions using <strong>Python</strong> is important.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8819019">Save This Job </a>
                                    <a class="show-more" jobId="8819019" href='/Jobs/Python-Developer-8819019.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Pontoon-Solutions-12830.aspx"><img alt="Pontoon Solutions" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/12830-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=cb73dafe2970234b4f8a15b05a8b6d31be2a8988fe6775f12de2a96d038a847e"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8826059" href='/Jobs/Python-Developer-9723-8826059.aspx' >Python Developer 9723</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Pontoon-Solutions-12830.aspx">Pontoon Solutions</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 29/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
<span>&nbsp;/</span>                                                <a href="/Jobs/Dublin-South/">Dublin South</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span><strong>Python</strong> Developer JP 9723 Dublin 6 months initial contract Hybrid - Flexible 3 days onsite and 2 days WFH Monday - Friday 9am - 5pm My high-profile <strong>Python</strong> Developer JP 9723</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8826059">Save This Job </a>
                                    <a class="show-more" jobId="8826059" href='/Jobs/Python-Developer-9723-8826059.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Stelfox-1626.aspx"><img alt="Stelfox" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1626-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=fca5c0061a2933f5e18cd12757f055bf8c9efbd2d158f007ab14c7c09dc4ee6b"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8818623" href='/Jobs/Back-End-Engineer-Python-8818623.aspx' >Back-End Engineer - Python</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Stelfox-1626.aspx">Stelfox</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€50,000 - €75,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 30/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
<span>&nbsp;/</span>                                                <a href="/Jobs/Dublin-South/">Dublin South</a>
<span>&nbsp;/</span>                                                <a href="/Jobs/Dublin-West/">Dublin West</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Solid knowledge of <strong>Python</strong> or Java programming, REST APIs, and Microservices architecture - An exciting Software Engineering opportunity with a leading U.S eCommerce company as they continue to build out their European Tech Hub in Dublin city. Our client provides a monthly subscription service to over 2 million customers in the US.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8818623">Save This Job </a>
                                    <a class="show-more" jobId="8818623" href='/Jobs/Back-End-Engineer-Python-8818623.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Stelfox-1626.aspx"><img alt="Stelfox" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1626-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=fca5c0061a2933f5e18cd12757f055bf8c9efbd2d158f007ab14c7c09dc4ee6b"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8817625" href='/Jobs/Python-Engineer-Daily-Rate-Contract-8817625.aspx' >Python Engineer - Daily Rate Contract Positions</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Stelfox-1626.aspx">Stelfox</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 28/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span><strong>Python</strong> Engineer - Daily Rates - Rolling Long-Term Contracts Exciting opportunities working on a global enterprise project solving complex business <strong>Python</strong> Engineer - Daily Rates - Rolling Long-Term Contracts - Comprehensive knowledge of <strong>Python</strong> Strong Linux/UNIX experience Experience building RESTful web APIs using <strong>Python</strong> frameworks such as Flask, Django</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8817625">Save This Job </a>
                                    <a class="show-more" jobId="8817625" href='/Jobs/Python-Engineer-Daily-Rate-Contract-8817625.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Brightwater-959.aspx"><img alt="Brightwater" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/959-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=8317abc2d4322b9ff0429a4e9e612661cc4ef3c30cf51a8de1fbb5e3cd27bf82"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8817228" href='/Jobs/Python-Developer-8817228.aspx' >Python Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Brightwater-959.aspx">Brightwater</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 28/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>They and have an immediate requirement for a number of <strong>Python</strong> developers, from junior to senior (including lead level) initially on a contract basis but which may become permanent. * <strong>Python</strong> 3.x <strong>Python</strong> Javascript vue - They About the Company - Our client is one of the largest and most successful companies in the world.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8817228">Save This Job </a>
                                    <a class="show-more" jobId="8817228" href='/Jobs/Python-Developer-8817228.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Morgan-McKinley-5478.aspx"><img alt="Morgan McKinley" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5478-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=e041799ef517bddfea9d49a50299f8ef2f92f64045e019956309b5c225581f9f"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8816637" href='/Jobs/Senopr-Python-Developer-8816637.aspx' >Senopr Python Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Morgan-McKinley-5478.aspx">Morgan McKinley</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 27/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Expertise in <strong>Python</strong>,Django and Flask and API development. Desing and Implement a radip growing <strong>python</strong> code base. Contruct APIs services within <strong>Python</strong> <strong>Python</strong> SQL REST Docker Flask Django - What you need: Minimum of 5 years professional experience. Excellent communication and - Minimum of 5 years professional experience.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8816637">Save This Job </a>
                                    <a class="show-more" jobId="8816637" href='/Jobs/Senopr-Python-Developer-8816637.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Spring-12827.aspx"><img alt="Spring" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/12827-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=178484c9ed6e6b2f4a3fee6be0c217d0d1aa2e13639a5f6cc1edf615528786fa"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8824033" href='/Jobs/Senior-Python-Developer-Contract-Ireland-8824033.aspx' >Senior Python Developer Contract Ireland 6-18 Months.</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Spring-12827.aspx">Spring</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€56.00 - €75.00 per hour</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 26/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>My client a leader in their business is in urgent need of a talented and experienced Senior <strong>Python</strong> developer to join them on a contract basis. My client is looking for a talented senior <strong>Python</strong> developer to work in the Risk Technology team.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8824033">Save This Job </a>
                                    <a class="show-more" jobId="8824033" href='/Jobs/Senior-Python-Developer-Contract-Ireland-8824033.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Brightwater-959.aspx"><img alt="Brightwater" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/959-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=8317abc2d4322b9ff0429a4e9e612661cc4ef3c30cf51a8de1fbb5e3cd27bf82"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8827618" href='/Jobs/Software-Engineers-Python-All-Levels-8827618.aspx' >Software Engineers - Python – All Levels</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Brightwater-959.aspx">Brightwater</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€70,000 - €140,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 03/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>They and have an immediate requirement for Software Engineers specialising in <strong>Python</strong> to join on a contract basis and to work on very interesting technical projects. My client is building a team to work on an all-new project and they have immediate opportunities for a talented Software Engineers with a focus on <strong>Python</strong> to join their team. * <strong>Python</strong> 3.x</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8827618">Save This Job </a>
                                    <a class="show-more" jobId="8827618" href='/Jobs/Software-Engineers-Python-All-Levels-8827618.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Brightwater-959.aspx"><img alt="Brightwater" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/959-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=8317abc2d4322b9ff0429a4e9e612661cc4ef3c30cf51a8de1fbb5e3cd27bf82"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8827617" href='/Jobs/Software-Engineer-Python-8827617.aspx' >Software Engineer- Python</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Brightwater-959.aspx">Brightwater</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€103,500 - €126,500 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 03/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>My client has an immediate requirement for a talented senior <strong>Python</strong> developer to work in the Risk & Finance Technology team. You will be responsible for designing and developing web-based <strong>Python</strong> solutions to help solve complex business problems within one of the most interesting parts of one of the world’s largest banks. Comprehensive knowledge of <strong>Python</strong></span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8827617">Save This Job </a>
                                    <a class="show-more" jobId="8827617" href='/Jobs/Software-Engineer-Python-8827617.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/EOLAS-IT-RECRUITMENT-SPECIALISTS-JOBS-824.aspx"><img alt="EOLAS – IT RECRUITMENT SPECIALISTS JOBS" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/824-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=8cb4c635d6adead42df2b9eb84b077f1b28778e73937bea1752c10c51daa30cc"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8820055" href='/Jobs/Data-Engineer-Python-and-Power-8820055.aspx' >Data Engineer – Python and Power BI</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/EOLAS-IT-RECRUITMENT-SPECIALISTS-JOBS-824.aspx">EOLAS – IT RECRUITMENT SPECIALISTS JOBS</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 03/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Nationwide/">Nationwide</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>The ideal candidate would have knowledge around Power BI and <strong>Python</strong> Development. * Excellent <strong>Python</strong> Development skills <strong>Python</strong> Data Engineer Data Administrator Power BI SQL Data Analysis - Our large International Financial Services client is looking for a talented Data Engineer to join their busy team. The ideal candidate would have</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8820055">Save This Job </a>
                                    <a class="show-more" jobId="8820055" href='/Jobs/Data-Engineer-Python-and-Power-8820055.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Archer-Recruitment-3823.aspx"><img alt="Archer Recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/3823-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=ddbc9c173878827ef6f9c8979e1e657be26be46028c44cef9c15a6984d3022e5"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8827178" href='/Jobs/QA-Automation-Engineer-Cloud-Python-8827178.aspx' >QA Automation Engineer - Cloud & Python - Contract</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Archer-Recruitment-3823.aspx">Archer Recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€110,000 - €125,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 02/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>QA Automation Engineer – Cloud and <strong>Python</strong> - Day Rate Contract Greenfield projects Upskill in modern tech stack, Cloud, CI/CD and Docker - QA Automation Engineer – Cloud and <strong>Python</strong> - Day Rate Contract - As a QA Automation Engineer, utilising <strong>Python,</strong> you will produce high-value web-based Automation solutions while also deepening your analytical and database experience!</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8827178">Save This Job </a>
                                    <a class="show-more" jobId="8827178" href='/Jobs/QA-Automation-Engineer-Cloud-Python-8827178.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/REALTIME-recruitment-3053.aspx"><img alt="REALTIME recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/3053-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=af8b091bd6d65059f23b9006acfb7306dd1f677bed0d5fcb8e76d4057358b8e3"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8824642" href='/Jobs/Principal-Engineer-Spark-Expert-AWS-8824642.aspx' >Principal Engineer - Spark Expert + AWS + Python/Scala + Google Cloud</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/REALTIME-recruitment-3053.aspx">REALTIME recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€90,000 - €125,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 27/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin-South/">Dublin South</a>
<span>&nbsp;/</span>                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Expertise in <strong>Python</strong> and Scala (Java desirable). Scala Spark <strong>Python</strong> AWS Google Cloud Java - Spark Principal Engineer Are you looking to make an immediate impact at a company that welcomes diverse and bold thinking? We are looking for someone - Spark Principal Engineer</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8824642">Save This Job </a>
                                    <a class="show-more" jobId="8824642" href='/Jobs/Principal-Engineer-Spark-Expert-AWS-8824642.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/EOLAS-IT-RECRUITMENT-SPECIALISTS-JOBS-824.aspx"><img alt="EOLAS – IT RECRUITMENT SPECIALISTS JOBS" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/824-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=8cb4c635d6adead42df2b9eb84b077f1b28778e73937bea1752c10c51daa30cc"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8816486" href='/Jobs/QA-Automation-Engineer-Python-8816486.aspx' >QA Automation Engineer - Python</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/EOLAS-IT-RECRUITMENT-SPECIALISTS-JOBS-824.aspx">EOLAS – IT RECRUITMENT SPECIALISTS JOBS</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€60,000 - €80,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 27/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Someone with good <strong>python</strong> coding skills (test will be provided in <strong>Python)</strong> QA Automation QA Automation Engineer Test Automation Engineer <strong>Python</strong> test engineer Software Developer in test - QA Test Automation Engineer One of the world’s leading Fintech firms is looking for an experienced Test Automation Engineer to join their team on a</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8816486">Save This Job </a>
                                    <a class="show-more" jobId="8816486" href='/Jobs/QA-Automation-Engineer-Python-8816486.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830176" href='/Jobs/Senior-Data-Engineer-8830176.aspx' >Senior Data Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€120,000 - €132,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 08/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span><strong>Python</strong> Initial 12 month Contract (extensions expected) Location: Dublin, Ireland - Rate: Competitive - An exciting new opportunity has opened up for a Senior Data Engineer to join my high-profile, global client, based in Dublin, Ireland. This is an initial 12 month contract with assurance to extend. This client are focusing on a key migration project to Snowflake.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830176">Save This Job </a>
                                    <a class="show-more" jobId="8830176" href='/Jobs/Senior-Data-Engineer-8830176.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Frank-Recruitment-Group-13018.aspx"><img alt="Frank Recruitment Group" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/13018-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=373371cfc3144e13dddd3682bf4488e4a572f114bcf7da9df155dfb03e46f356"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8831402" href='/Jobs/Senior-Software-Developer-8831402.aspx' >Senior Software Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Frank-Recruitment-Group-13018.aspx">Frank Recruitment Group</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€65,000 - €85,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Tech stack: Java 8, <strong>Python,</strong> Spring, RESTful webservices, Apache Camel, ActiveMQ, AWS, Kubernetes, Terraform, API, Oracle, Postgres, NoSQL DB, PL/SQL, JMeter, Jenkins, Sonar, Maven, Git, Docker/Containerization. * 5+ years working on application design and development with Java/<strong>Python,</strong> OOP, Spring, JMS, Camel, Leveraging AWS infrastructure - Java <strong>Python</strong> Aws</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8831402">Save This Job </a>
                                    <a class="show-more" jobId="8831402" href='/Jobs/Senior-Software-Developer-8831402.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Workday-7414.aspx"><img alt="Workday" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/7414-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7308a8f75f890791dd2dbe84b027303287555793ca684356bc2421e983de2745"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8824444" href='/Jobs/Scala-Engineer-8824444.aspx' >Scala Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Workday-7414.aspx">Workday</a>
                                            </h3>
                                        
  <style data-styled="fLtnCS" data-styled-version="4.4.0">
/* sc-component-id: Star__StyledSvg-sc-1ge1c9k-0 */
.sky-component .fLtnCS{margin:0 1px;width:21px;height:21px;}</style>

  

  <div id="sky-65aace24e2b188e9-3" class="sky-component ZG9udXQ"><div><div class="sky-search-rating"><div class="sky-search-rating__stars"><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0qbbcb20jb5" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0qbbcb20jb5)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0pjvtlbtdyvj" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0pjvtlbtdyvj)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0vlut0svsg8" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0vlut0svsg8)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0etfls5a82o" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0etfls5a82o)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0v7ou71cbj3a" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="50%" style="stop-color:#f3d756"></stop><stop offset="50%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0v7ou71cbj3a)" stroke="#f3d756"></path></svg></div><div class="sky-search-rating__reviews-count">9<!-- --> company<!-- --> <!-- -->reviews</div></div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-3",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"7414","data":{"localId":"7414","surveysCount":9,"overallRatingAvg":4.37855,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>3+ years of distributed systems engineering experience utilizing one or more of the following: Java, Scala, <strong>Python,</strong> Golang - Do what you love. Love what you do. At Workday, we help the world's largest organizations adapt to what's next by bringing finance, HR, and planning</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8824444">Save This Job </a>
                                    <a class="show-more" jobId="8824444" href='/Jobs/Scala-Engineer-8824444.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Workday-7414.aspx"><img alt="Workday" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/7414-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7308a8f75f890791dd2dbe84b027303287555793ca684356bc2421e983de2745"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8827306" href='/Jobs/Java-Development-Engineer-Big-Data-8827306.aspx' >Java Development Engineer - Big Data Cloud</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Workday-7414.aspx">Workday</a>
                                            </h3>
                                        
  <style data-styled="fLtnCS" data-styled-version="4.4.0">
/* sc-component-id: Star__StyledSvg-sc-1ge1c9k-0 */
.sky-component .fLtnCS{margin:0 1px;width:21px;height:21px;}</style>

  

  <div id="sky-65aace24e2b188e9-3" class="sky-component ZG9udXQ"><div><div class="sky-search-rating"><div class="sky-search-rating__stars"><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0qbbcb20jb5" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0qbbcb20jb5)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0pjvtlbtdyvj" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0pjvtlbtdyvj)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0vlut0svsg8" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0vlut0svsg8)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0etfls5a82o" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0etfls5a82o)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0v7ou71cbj3a" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="50%" style="stop-color:#f3d756"></stop><stop offset="50%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0v7ou71cbj3a)" stroke="#f3d756"></path></svg></div><div class="sky-search-rating__reviews-count">9<!-- --> company<!-- --> <!-- -->reviews</div></div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-3",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"7414","data":{"localId":"7414","surveysCount":9,"overallRatingAvg":4.37855,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Proficient in Java/Scala programming and one scripting language, ruby/<strong>python</strong> preferred. Do what you love. Love what you do. At Workday, we help the world's largest organizations adapt to what's next by bringing finance, HR, and planning</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8827306">Save This Job </a>
                                    <a class="show-more" jobId="8827306" href='/Jobs/Java-Development-Engineer-Big-Data-8827306.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/itContracting-5819.aspx"><img alt="itContracting" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5819-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=81e1d3d4b21488b361128c75d36a33b83c24bd1e43b9e7eb42df6e2b7edde8a0"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8823308" href='/Jobs/Software-Engineer-8823308.aspx' >Software Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/itContracting-5819.aspx">itContracting</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Proficiency with several languages (e.g. <strong>Python,</strong> JavaScript, Typescript, React, NodeJS, SQL) <strong>Python,</strong> JavaScript RESTful or GraphQL APIs AWS - itContracting are currently seeking applicants for a Software Engineer. This is a permanent position located with our client in Belfast (Hybrid</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8823308">Save This Job </a>
                                    <a class="show-more" jobId="8823308" href='/Jobs/Software-Engineer-8823308.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Workday-7414.aspx"><img alt="Workday" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/7414-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7308a8f75f890791dd2dbe84b027303287555793ca684356bc2421e983de2745"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8827313" href='/Jobs/Java-Software-Engineer-8827313.aspx' >Java Software Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Workday-7414.aspx">Workday</a>
                                            </h3>
                                        
  <style data-styled="fLtnCS" data-styled-version="4.4.0">
/* sc-component-id: Star__StyledSvg-sc-1ge1c9k-0 */
.sky-component .fLtnCS{margin:0 1px;width:21px;height:21px;}</style>

  

  <div id="sky-65aace24e2b188e9-3" class="sky-component ZG9udXQ"><div><div class="sky-search-rating"><div class="sky-search-rating__stars"><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0qbbcb20jb5" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0qbbcb20jb5)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0pjvtlbtdyvj" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0pjvtlbtdyvj)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0vlut0svsg8" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0vlut0svsg8)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0etfls5a82o" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0etfls5a82o)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0v7ou71cbj3a" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="50%" style="stop-color:#f3d756"></stop><stop offset="50%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0v7ou71cbj3a)" stroke="#f3d756"></path></svg></div><div class="sky-search-rating__reviews-count">9<!-- --> company<!-- --> <!-- -->reviews</div></div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-3",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"7414","data":{"localId":"7414","surveysCount":9,"overallRatingAvg":4.37855,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>1 + years of distributed systems engineering experience utilizing one or more of the following: Java, Scala, <strong>Python,</strong> Golang * 2+ years of distributed systems engineering experience utilizing one or more of the following: Java, Scala, <strong>Python,</strong> Golang - Do what you love. Love what you do.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8827313">Save This Job </a>
                                    <a class="show-more" jobId="8827313" href='/Jobs/Java-Software-Engineer-8827313.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830184" href='/Jobs/Principal-Software-Engineer-8830184.aspx' >Principal Software Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€115,000 - €125,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 08/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Experience with Java, Javascript, C#, ReactJS, Angular, VueJS, NodeJs, Azure, AWS, Google Cloud , DevOps, <strong>Python,</strong> Java, GoLang - Salary: €115,000 - €125,000 - Remote Working (Within Ireland) One of the world's biggest and most innovative Tech companies has decided they will be centralising all their development operations to Ireland.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830184">Save This Job </a>
                                    <a class="show-more" jobId="8830184" href='/Jobs/Principal-Software-Engineer-8830184.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8829318" href='/Jobs/Software-Architect-8829318.aspx' >Software Architect</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€110,000 - €120,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 05/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span><strong>Python</strong> | React | NodeJS | AWS - The preferred tech stack for the role is NodeJS and React however experience with <strong>Python</strong> can be considered. * Experience with <strong>Python,</strong> NodeJS, React - Architect Software <strong>Python</strong> Nodejs React AWS - Location - Dublin - Permanent Full-Time - Job Description</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8829318">Save This Job </a>
                                    <a class="show-more" jobId="8829318" href='/Jobs/Software-Architect-8829318.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Archer-Recruitment-3823.aspx"><img alt="Archer Recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/3823-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=ddbc9c173878827ef6f9c8979e1e657be26be46028c44cef9c15a6984d3022e5"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8821899" href='/Jobs/Senior-DevOps-Step-to-lead-8821899.aspx' >Senior DevOps - Step to lead</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Archer-Recruitment-3823.aspx">Archer Recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 06/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>devops aws hashicorp terraform kubernetes <strong>python</strong> devops * Fully-remote * Kubernetes implementation * Pipeline migration - A unique opportunity for an experienced DevOps Engineer to join a global software company as one of their first hires in DevOps. You’ll have the opportunity to build a function as you see fit, from the ground up.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8821899">Save This Job </a>
                                    <a class="show-more" jobId="8821899" href='/Jobs/Senior-DevOps-Step-to-lead-8821899.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8822610" href='/Jobs/Software-Engineer-8822610.aspx' >Software Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€70,000 - €80,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 07/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>You will work in conjunction with the <strong>Python</strong>/AI team building a new product, and continuing to add new features to their existing products - all powered by AI of course. Dublin City Centre (Fully Remote) Up to €80K p/a + Equity, Bonus, Healthcare etc - Tech Stack - Scala (Scala exp not essential), Play, AWS, Terraform, K8s</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8822610">Save This Job </a>
                                    <a class="show-more" jobId="8822610" href='/Jobs/Software-Engineer-8822610.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Intel-1568.aspx"><img alt="Intel" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1568-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=6cdb464e00dd8d2fa804fc25cb086028d241e694363c84925317e6cb0c837663"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8831121" href='/Jobs/Module-Data-Science-Engineer-8831121.aspx' >Module Data Science Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Intel-1568.aspx">Intel</a>
                                            </h3>
                                        
  <style data-styled="fLtnCS" data-styled-version="4.4.0">
/* sc-component-id: Star__StyledSvg-sc-1ge1c9k-0 */
.sky-component .fLtnCS{margin:0 1px;width:21px;height:21px;}</style>

  

  <div id="sky-65aace24e2b188e9-4" class="sky-component ZG9udXQ"><div><div class="sky-search-rating"><div class="sky-search-rating__stars"><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0hl9alxdi9av" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0hl9alxdi9av)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0gja3pe63g9" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0gja3pe63g9)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient07viw2nzwb9" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient07viw2nzwb9)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0hdpm28xwb8u" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="65%" style="stop-color:#f3d756"></stop><stop offset="65%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0hdpm28xwb8u)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0dc2oymlp036" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:#f3d756"></stop><stop offset="0%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0dc2oymlp036)" stroke="#f3d756"></path></svg></div><div class="sky-search-rating__reviews-count">73<!-- --> company<!-- --> <!-- -->reviews</div></div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-4",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"1568","data":{"localId":"1568","surveysCount":73,"overallRatingAvg":3.84421,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Kildare/">Kildare</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>2+ years in data analytics and relational databases (<strong>Python,</strong> SQL, dashboards, APC, machine learning, etc) * 3+ years in data analytics and relational databases (<strong>Python,</strong> SQL, dashboards, APC, machine learning, etc) Job Description FSM's Equipment Productivity Group is hiring a Senior Data Science Engineer to focus on Module Data Solutions. With Intel's ambitious</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8831121">Save This Job </a>
                                    <a class="show-more" jobId="8831121" href='/Jobs/Module-Data-Science-Engineer-8831121.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8820529" href='/Jobs/Software-Engineer-8820529.aspx' >Software  Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€45,000 - €60,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 04/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>1 year experience with <strong>Python</strong> C++ <strong>Python</strong> Measurement QT - Location: Dublin (Hybrid Working 2/3 Days) A great company, growing very quickly are looking to further expand out their software team. Join this great, close knit specialist team in their market unique product. The company are focused around creating measurement tools among areas such as RF.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8820529">Save This Job </a>
                                    <a class="show-more" jobId="8820529" href='/Jobs/Software-Engineer-8820529.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Harvey-Nash-1058.aspx"><img alt="Harvey Nash" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1058-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=1b488998cbefc678332a5d92b4a9dd9a1d7c831596f94c6bb8dc118dc0767952"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8824983" href='/Jobs/Software-Engineer-Ruby-on-Rails-8824983.aspx' >Software Engineer - Ruby on Rails - Fully Remote</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Harvey-Nash-1058.aspx">Harvey Nash</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€80,000 - €85,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 04/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Experience developing with a dynamic programming language i.e. Ruby, <strong>Python,</strong> Go, JavaScript, PHP - Ruby on Rails RoR Ruby <strong>Python</strong> go - My client is an award-winning company who is on an unprecedented growth trajectory and looking for people who want to do great things. They help companies stand out by giving them new ways to engage with buyers and customers.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8824983">Save This Job </a>
                                    <a class="show-more" jobId="8824983" href='/Jobs/Software-Engineer-Ruby-on-Rails-8824983.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Life-Science-Recruitment-4197.aspx"><img alt="Life Science Recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/4197-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=3e9c3edcab358b91d93889cf54c937e379df10805a978d84ceff926ccd712328"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8823618" href='/Jobs/Technical-Scientist-8823618.aspx' >Technical Scientist</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Life-Science-Recruitment-4197.aspx">Life Science Recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Cork/">Cork</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Familiarity with programming languages (e.g.: Java, <strong>Python,</strong> r, Regex, HTML) required. RK9171 Contract – 12 months - Cork (Remote) We’re currently recruiting for an exciting opportunity with an award-winning Pharmaceutical organization based in Cork.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8823618">Save This Job </a>
                                    <a class="show-more" jobId="8823618" href='/Jobs/Technical-Scientist-8823618.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Workday-7414.aspx"><img alt="Workday" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/7414-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7308a8f75f890791dd2dbe84b027303287555793ca684356bc2421e983de2745"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8823107" href='/Jobs/Software-Development-Engineer-8823107.aspx' >Software Development Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Workday-7414.aspx">Workday</a>
                                            </h3>
                                        
  <style data-styled="fLtnCS" data-styled-version="4.4.0">
/* sc-component-id: Star__StyledSvg-sc-1ge1c9k-0 */
.sky-component .fLtnCS{margin:0 1px;width:21px;height:21px;}</style>

  

  <div id="sky-65aace24e2b188e9-3" class="sky-component ZG9udXQ"><div><div class="sky-search-rating"><div class="sky-search-rating__stars"><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0qbbcb20jb5" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0qbbcb20jb5)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0pjvtlbtdyvj" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0pjvtlbtdyvj)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0vlut0svsg8" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0vlut0svsg8)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0etfls5a82o" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0etfls5a82o)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0v7ou71cbj3a" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="50%" style="stop-color:#f3d756"></stop><stop offset="50%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0v7ou71cbj3a)" stroke="#f3d756"></path></svg></div><div class="sky-search-rating__reviews-count">9<!-- --> company<!-- --> <!-- -->reviews</div></div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-3",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"7414","data":{"localId":"7414","surveysCount":9,"overallRatingAvg":4.37855,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 08/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>4 years of engineering experience using one or more of the following: Java, Scala, <strong>Python,</strong> Golang - Do what you love. Love what you do. At Workday, we help the world's largest organizations adapt to what's next by bringing finance, HR, and planning</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8823107">Save This Job </a>
                                    <a class="show-more" jobId="8823107" href='/Jobs/Software-Development-Engineer-8823107.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result highlighted ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Xilinx-part-of-AMD-6907.aspx"><img alt="Xilinx part of AMD" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/6907-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=4ee39ea72eeb016c4a80a7fe75f68ea086d1517f1c2591b1738ae2f10393ea7e"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8826372" href='/Jobs/Design-Verification-Engineer-8826372.aspx?hl=45|application_confirmed' >Design/Verification Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Xilinx-part-of-AMD-6907.aspx">Xilinx part of AMD</a>
                                            </h3>
                                        
  <style data-styled="" data-styled-version="4.4.0"></style>

  

  <div id="sky-65aace24e2b188e9-5" class="sky-component ZG9udXQ"><div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-5",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"6907","data":{"localId":"6907","surveysCount":7,"overallRatingAvg":2.69086,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Belfast/">Belfast</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Familiarity with scripting languages: <strong>Python,</strong> Tcl, Perl - Xilinx is now part of Advanced Micro Devices (AMD). At AMD, we push the boundaries of what is possible. We believe in changing the world for the</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8826372">Save This Job </a>
                                    <a class="show-more" jobId="8826372" href='/Jobs/Design-Verification-Engineer-8826372.aspx?hl=45|application_confirmed'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/MCS-Group-Consultancy-14357.aspx"><img alt="MCS Group Consultancy" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/14357-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=05e786affa6a71e20e23078193b3f5850c1e3231678f1a214a57ab65c226d223"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8823631" href='/Jobs/Senior-Machine-Learning-Engineer-8823631.aspx' >Senior Machine Learning Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/MCS-Group-Consultancy-14357.aspx">MCS Group Consultancy</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€80,000 - €90,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>You will have a strong academic record in Maths / Physics or other engineering related subjects, proficient in <strong>Python</strong> and experience interacting with machine learning / deep learning tools like Pytorch is beneficial. Mathematical Theory Optimisation <strong>Python</strong> Machine Learning Deep Learning Pytorch Algorithms</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8823631">Save This Job </a>
                                    <a class="show-more" jobId="8823631" href='/Jobs/Senior-Machine-Learning-Engineer-8823631.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/itContracting-5819.aspx"><img alt="itContracting" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5819-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=81e1d3d4b21488b361128c75d36a33b83c24bd1e43b9e7eb42df6e2b7edde8a0"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8828936" href='/Jobs/Senior-Data-Engineer-8828936.aspx' >Senior Data Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/itContracting-5819.aspx">itContracting</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 05/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Extensive experience using <strong>python</strong> to deliver data engineering solutions. <strong>Python</strong> Azure SQL - itContracting are seeking applications for a Senior Data Engineer, this is a permanent hybrid position located in Dublin 24. Requirements: Azure/AWS * Azure/AWS Experience (3 years). Azure Data Certification a plus</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8828936">Save This Job </a>
                                    <a class="show-more" jobId="8828936" href='/Jobs/Senior-Data-Engineer-8828936.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830191" href='/Jobs/Azure-Systems-Admin-8830191.aspx' >Azure Systems Admin</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€108,000 - €132,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 08/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Strong Powershell/Bash/<strong>Python</strong> scripting for process automations * Fully work from home available * 6-Month rolling contract * Cloud migration projects for a multinational</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830191">Save This Job </a>
                                    <a class="show-more" jobId="8830191" href='/Jobs/Azure-Systems-Admin-8830191.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Stelfox-1626.aspx"><img alt="Stelfox" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1626-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=fca5c0061a2933f5e18cd12757f055bf8c9efbd2d158f007ab14c7c09dc4ee6b"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8827499" href='/Jobs/Senior-Cloud-Developer-Great-Daily-8827499.aspx' >Senior Cloud Developer - Great Daily Rates</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Stelfox-1626.aspx">Stelfox</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 03/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Core Java, <strong>Python</strong> (and frameworks). Senior Cloud Developer - Contractor Role My client is a global financial services organisation looking for an experienced Cloud Developer to join - Senior Cloud Developer - Contractor Role - My client is a global financial services organisation looking for an experienced Cloud Developer to join their Cloud Platforms group.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8827499">Save This Job </a>
                                    <a class="show-more" jobId="8827499" href='/Jobs/Senior-Cloud-Developer-Great-Daily-8827499.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Azon-7502.aspx"><img alt="Azon" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/7502-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=a0a1c660415d6330bad2884d2099effff6b262dcc2118bb2f3a04d266dc2a344"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8827161" href='/Jobs/Senior-Full-Stack-Developer-18-8827161.aspx' >Senior Full Stack Developer (18 month FTC)</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Azon-7502.aspx">Azon</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 02/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Proficiency with server-side languages such as <strong>Python,</strong> and .NET - Senior Full Stack Developer (18 months with possibility of extension) We have partnered with one of the largest reinsurance groups in the world to - Senior Full Stack Developer (18 months with possibility of extension)</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8827161">Save This Job </a>
                                    <a class="show-more" jobId="8827161" href='/Jobs/Senior-Full-Stack-Developer-18-8827161.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/REALTIME-recruitment-3053.aspx"><img alt="REALTIME recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/3053-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=af8b091bd6d65059f23b9006acfb7306dd1f677bed0d5fcb8e76d4057358b8e3"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8823582" href='/Jobs/Senior-DevOps-Engineer-to-design-8823582.aspx' >Senior DevOps Engineer, to design, develop, deploy & maintain systems. You will focus on automation</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/REALTIME-recruitment-3053.aspx">REALTIME recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Scripting skills: Bash, <strong>Python,</strong> Ruby, PHP, etc - DevOps Agile Linux API AWS <strong>Python</strong> Java - RealTime are looking for a Senior DevOps Engineer, to design, develop, deploy & maintain systems. You will focus on automation & configuration - You will focus on automation & configuration of the management & monitoring environment.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8823582">Save This Job </a>
                                    <a class="show-more" jobId="8823582" href='/Jobs/Senior-DevOps-Engineer-to-design-8823582.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Globalization-Partners-14137.aspx"><img alt="Globalization Partners" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/14137-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=1821834896e7a7f7a92d56ecfd8b146e62c5224c29f2e6da9741924dcefa86c2"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8824452" href='/Jobs/Principal-Software-Engineer-in-Test-8824452.aspx' >Principal Software Engineer in Test</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Globalization-Partners-14137.aspx">Globalization Partners</a>
                                            </h3>
                                        
  <style data-styled="fLtnCS" data-styled-version="4.4.0">
/* sc-component-id: Star__StyledSvg-sc-1ge1c9k-0 */
.sky-component .fLtnCS{margin:0 1px;width:21px;height:21px;}</style>

  

  <div id="sky-65aace24e2b188e9-6" class="sky-component ZG9udXQ"><div><div class="sky-search-rating"><div class="sky-search-rating__stars"><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0433cg5jtm6g" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0433cg5jtm6g)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0bq2vp16t6ia" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0bq2vp16t6ia)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0alt1i2c0lb" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0alt1i2c0lb)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0luhxjrw7hg" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0luhxjrw7hg)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0tmpvgdoqh7b" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0tmpvgdoqh7b)" stroke="#f3d756"></path></svg></div><div class="sky-search-rating__reviews-count">2<!-- --> company<!-- --> <!-- -->reviews</div></div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-6",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"14137","data":{"localId":"14137","surveysCount":2,"overallRatingAvg":5,"linkType":"COMPANY_PROFILE_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 03/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Galway/">Galway</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Strong programming experience with JavaScript/Typescript preferably, alternatively Java, <strong>Python,</strong> C# or similar language.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8824452">Save This Job </a>
                                    <a class="show-more" jobId="8824452" href='/Jobs/Principal-Software-Engineer-in-Test-8824452.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Solas-IT-Recruitment-4746.aspx"><img alt="Solas IT  Recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/4746-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=087976938dac89f20578824f6fd3898517486692b2757bf96bf91194879224ce"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830370" href='/Jobs/Full-Stack-Developer-React-8830370.aspx' >Full Stack Developer - React</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Solas-IT-Recruitment-4746.aspx">Solas IT  Recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€70,000 - €80,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>2+ years’ experience working in server-side development using object-oriented languages (e.g.: C#, Java, <strong>Python</strong> or similar). "React" "Typescript" "Java" "<strong>Python"</strong> Their clients include some of the biggest banks in the world. Due to their - My client is a Global Fintech company.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830370">Save This Job </a>
                                    <a class="show-more" jobId="8830370" href='/Jobs/Full-Stack-Developer-React-8830370.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Archer-Recruitment-3823.aspx"><img alt="Archer Recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/3823-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=ddbc9c173878827ef6f9c8979e1e657be26be46028c44cef9c15a6984d3022e5"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830750" href='/Jobs/Data-Analyst-Telematics-Projects-8830750.aspx' >Data Analyst - Telematics Projects!</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Archer-Recruitment-3823.aspx">Archer Recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€60,000 - €80,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Using tools such as <strong>Python,</strong> SQL and Tableau, you will be a part of a fast-paced environment and tackle complex projects. You will also test your <strong>Python</strong> and Tableau skills in solving business problems that will have you placing your stamp on the company. * 3+ years <strong>Python</strong> and SQL experience. "Data Analysis" "SQL" "AWS" "<strong>Python"</strong> "Tableau" "Visualisation"</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830750">Save This Job </a>
                                    <a class="show-more" jobId="8830750" href='/Jobs/Data-Analyst-Telematics-Projects-8830750.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Verizon-747.aspx"><img alt="Verizon" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/747-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=5a608627acf9e79087f29a851b66529bd31cfa8cb94ffbe06bd81623f6739198"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8825472" href='/Jobs/Senior-Systems-Engineer-DevOps-8825472.aspx' >Senior Systems Engineer - DevOps</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Verizon-747.aspx">Verizon</a>
                                            </h3>
                                        
                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 05/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Experience automating operational tasks in at least one of the following: <strong>Python,</strong> BASH. Verizon is one of the world’s leading providers of technology and communications services, transforming the way we connect across the globe. We’re a - We’re a diverse network of people driven by our shared ambition to shape a better future.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8825472">Save This Job </a>
                                    <a class="show-more" jobId="8825472" href='/Jobs/Senior-Systems-Engineer-DevOps-8825472.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Oliver-James-4598.aspx"><img alt="Oliver James" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/4598-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=02e5f31b279010bcf84714848660f6c25dd998917952e289d7719536f476c97a"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830689" href='/Jobs/Senior-Investment-Analyst-8830689.aspx' >Senior Investment Analyst</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Oliver-James-4598.aspx">Oliver James</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
<span>&nbsp;/</span>                                                <a href="/Jobs/Dublin-North/">Dublin North</a>
<span>&nbsp;/</span>                                                <a href="/Jobs/Dublin-City-Centre/">Dublin City Centre</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>A high level of proficiency with Microsoft applications including Excel, Powerpoint and Word is required while experience with Bloomberg, MSCI BarraOne, RiskMetrics, R, <strong>Python</strong> or similar would be beneficial; * Analysing the investment performance of client portfolios for the Management Company (both UCITS and AIFMD)</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830689">Save This Job </a>
                                    <a class="show-more" jobId="8830689" href='/Jobs/Senior-Investment-Analyst-8830689.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8822869" href='/Jobs/Business-Intelligence-Developer-8822869.aspx' >Business Intelligence Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€55,000 - €65,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 07/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Knowledge of <strong>Python</strong> (Pandas) is preferred however not necessary - Salary: €55-65,000 - My client, a financial giant, have asked me to help recruit an experienced business intelligence analyst. * Constant monitoring of the business intelligence space to ensure the client keeps with the change. * Be able to perform adhoc analysis as and when required</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8822869">Save This Job </a>
                                    <a class="show-more" jobId="8822869" href='/Jobs/Business-Intelligence-Developer-8822869.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8826256" href='/Jobs/Lead-Software-Developer-8826256.aspx' >Lead Software Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€85,000 - €95,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 29/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span><strong>Python</strong> experience 5+ years - Lead <strong>Python</strong> React Fullstack Developer Engineer - Lead Software Engineer Location - Dublin/Remote Permanent Full-Time Job Description I am working with a hugely successful tech company based in Dublin - Lead Software Engineer - Location - Dublin/Remote - Permanent Full-Time - Job Description</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8826256">Save This Job </a>
                                    <a class="show-more" jobId="8826256" href='/Jobs/Lead-Software-Developer-8826256.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830517" href='/Jobs/DataOps-Engineer-8830517.aspx' >DataOps Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€55,000 - €70,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Programming experience, preferably <strong>Python</strong> or Scala - DataOps ETL <strong>Python</strong> Airflow ClickHouse Snowflake SQL - This company - We're working closely with a global advertising company who have ambitious plans to expand their IT presence in Ireland.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830517">Save This Job </a>
                                    <a class="show-more" jobId="8830517" href='/Jobs/DataOps-Engineer-8830517.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Solas-IT-Recruitment-4746.aspx"><img alt="Solas IT  Recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/4746-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=087976938dac89f20578824f6fd3898517486692b2757bf96bf91194879224ce"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830355" href='/Jobs/QA-Automation-Engineer-8830355.aspx' >QA Automation Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Solas-IT-Recruitment-4746.aspx">Solas IT  Recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€65,000 - €75,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Languages/Tools: <strong>Python,</strong> JavaScript, SQL, Test Rails, Jenkins, Bitbucket, Jira "qa" "<strong>python"</strong> "automation" My client is a strongly backed US Start-up who are building their development team in Ireland. The company are an enterprise IT Asset Management - The company are an enterprise IT Asset Management company.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830355">Save This Job </a>
                                    <a class="show-more" jobId="8830355" href='/Jobs/QA-Automation-Engineer-8830355.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Archer-Recruitment-3823.aspx"><img alt="Archer Recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/3823-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=ddbc9c173878827ef6f9c8979e1e657be26be46028c44cef9c15a6984d3022e5"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8823535" href='/Jobs/Data-Engineer-12-month-Contract-8823535.aspx' >Data Engineer  - 12 month Contract (€517 per day)</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Archer-Recruitment-3823.aspx">Archer Recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€100,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Using snowflake and oracle will be responsible for designing, developing and implementing a <strong>python</strong> application - This opportunity would ideally suit an experienced individual with a strong oracle background and strong <strong>python</strong> skills who is well established and has an expertise in all end to end developments of the oracle suite. * Oracle/ snowflake and <strong>python</strong></span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8823535">Save This Job </a>
                                    <a class="show-more" jobId="8823535" href='/Jobs/Data-Engineer-12-month-Contract-8823535.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Workday-7414.aspx"><img alt="Workday" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/7414-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7308a8f75f890791dd2dbe84b027303287555793ca684356bc2421e983de2745"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8829453" href='/Jobs/Software-Engineer-Site-Reliability-8829453.aspx' >Software Engineer - Site Reliability</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Workday-7414.aspx">Workday</a>
                                            </h3>
                                        
  <style data-styled="fLtnCS" data-styled-version="4.4.0">
/* sc-component-id: Star__StyledSvg-sc-1ge1c9k-0 */
.sky-component .fLtnCS{margin:0 1px;width:21px;height:21px;}</style>

  

  <div id="sky-65aace24e2b188e9-3" class="sky-component ZG9udXQ"><div><div class="sky-search-rating"><div class="sky-search-rating__stars"><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0qbbcb20jb5" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0qbbcb20jb5)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0pjvtlbtdyvj" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0pjvtlbtdyvj)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0vlut0svsg8" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0vlut0svsg8)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0etfls5a82o" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0etfls5a82o)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0v7ou71cbj3a" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="50%" style="stop-color:#f3d756"></stop><stop offset="50%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0v7ou71cbj3a)" stroke="#f3d756"></path></svg></div><div class="sky-search-rating__reviews-count">9<!-- --> company<!-- --> <!-- -->reviews</div></div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-3",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"7414","data":{"localId":"7414","surveysCount":9,"overallRatingAvg":4.37855,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 06/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>3+ years coding experience and can utilize various languages (We focus and build tooling and automation using <strong>Python,</strong> GoLang and Java.) Do what you love. Love what you do. At Workday, we help the world's largest organizations adapt to what's next by bringing finance, HR, and planning</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8829453">Save This Job </a>
                                    <a class="show-more" jobId="8829453" href='/Jobs/Software-Engineer-Site-Reliability-8829453.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Berkley-Recruitment-Group-2330.aspx"><img alt="Berkley Recruitment Group" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/2330-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=97eec2be052b1d01ac7a32f2add4fc5b28901736e56cc3aa0e75125a73636486"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830603" href='/Jobs/Technical-Administrator-8830603.aspx' >Technical Administrator</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Berkley-Recruitment-Group-2330.aspx">Berkley Recruitment Group</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€120,000 - €144,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Coding or scripting experience with PowerShell, Bash, <strong>Python</strong> Dublin My client, a multinational insurance company is looking for an experienced Technical Administrator to configure and maintain their infrastructure which includes testing, implementing, monitoring and tuning platforms to ensure availability and optimum systems performance.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830603">Save This Job </a>
                                    <a class="show-more" jobId="8830603" href='/Jobs/Technical-Administrator-8830603.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Xilinx-part-of-AMD-6907.aspx"><img alt="Xilinx part of AMD" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/6907-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=4ee39ea72eeb016c4a80a7fe75f68ea086d1517f1c2591b1738ae2f10393ea7e"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8823495" href='/Jobs/Verification-Engineer-8823495.aspx' >Verification Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Xilinx-part-of-AMD-6907.aspx">Xilinx part of AMD</a>
                                            </h3>
                                        
  <style data-styled="" data-styled-version="4.4.0"></style>

  

  <div id="sky-65aace24e2b188e9-5" class="sky-component ZG9udXQ"><div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-5",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"6907","data":{"localId":"6907","surveysCount":7,"overallRatingAvg":2.69086,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Knowledge of scripting languages (Perl/<strong>Python)</strong> would be an advantage. What you do at AMD changes everything At AMD, we push the boundaries of what is possible. We believe in changing the world for the better by driving - What you do at AMD changes everything - At AMD, we push the boundaries of what is possible.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8823495">Save This Job </a>
                                    <a class="show-more" jobId="8823495" href='/Jobs/Verification-Engineer-8823495.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/EOLAS-IT-RECRUITMENT-SPECIALISTS-JOBS-824.aspx"><img alt="EOLAS – IT RECRUITMENT SPECIALISTS JOBS" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/824-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=8cb4c635d6adead42df2b9eb84b077f1b28778e73937bea1752c10c51daa30cc"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8826266" href='/Jobs/Senior-Software-Engineer-8826266.aspx' >Senior Software Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/EOLAS-IT-RECRUITMENT-SPECIALISTS-JOBS-824.aspx">EOLAS – IT RECRUITMENT SPECIALISTS JOBS</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 05/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin-City-Centre/">Dublin City Centre</a>
<span>&nbsp;/</span>                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Develop fully functioning applications based on frameworks such as .Net & Spring/Spring Boot, & using languages including C#, Java, Scala, JavaScript, <strong>Python,</strong> & Go. My Dublin based client is recruiting for Senior Software Engineers to join the team on a permanent basis. You will work in a fast moving, agile</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8826266">Save This Job </a>
                                    <a class="show-more" jobId="8826266" href='/Jobs/Senior-Software-Engineer-8826266.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Stelfox-1626.aspx"><img alt="Stelfox" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1626-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=fca5c0061a2933f5e18cd12757f055bf8c9efbd2d158f007ab14c7c09dc4ee6b"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8820915" href='/Jobs/Fullstack-Engineer-8820915.aspx' >Fullstack Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Stelfox-1626.aspx">Stelfox</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 04/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Technologies used: Backends are written mostly in <strong>Python</strong> using Django as a framework (with a couple of Scala services mixed in), all running on Kubernetes , while our frontend is written in Typescript using React . Role Description My client run an interactive cloud-based presentation platform that helps users connect with their audience. We’re looking for a</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8820915">Save This Job </a>
                                    <a class="show-more" jobId="8820915" href='/Jobs/Fullstack-Engineer-8820915.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/ICDS-Recruitment-1623.aspx"><img alt="ICDS Recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1623-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=d0b099ba9028614adafd07265e839a457e75b11ee32af7d3ec1fe6f1c4ff5fca"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8820766" href='/Jobs/Senior-Software-Engineer-North-Dublin-8820766.aspx' >Senior Software Engineer - North Dublin</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/ICDS-Recruitment-1623.aspx">ICDS Recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 04/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
<span>&nbsp;/</span>                                                <a href="/Jobs/Dublin-North/">Dublin North</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>• Other software skills that would be an advantage are XAML, XAMARIN, Design patterns (MVVM), Scripting languages (<strong>Python,</strong> Lua, MS batch files), knowledge of assembly language, knowledge of source repositories. This role involves working on a wide range of projects related to medical device software, databases, data</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8820766">Save This Job </a>
                                    <a class="show-more" jobId="8820766" href='/Jobs/Senior-Software-Engineer-North-Dublin-8820766.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8821813" href='/Jobs/Data-Analyst-8821813.aspx' >Data Analyst</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€96,000 - €120,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 06/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span><strong>Python</strong> SQL Tableau <strong>Python</strong> Hi all, Hope things are well with yourselves! A great opportunity has arisen to join a healthcare company based in Limerick. Coming in as a Data - Hi all, Hope things are well with yourselves!</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8821813">Save This Job </a>
                                    <a class="show-more" jobId="8821813" href='/Jobs/Data-Analyst-8821813.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Azon-7502.aspx"><img alt="Azon" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/7502-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=a0a1c660415d6330bad2884d2099effff6b262dcc2118bb2f3a04d266dc2a344"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8827160" href='/Jobs/Senior-Software-Developer-8827160.aspx' >Senior Software Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Azon-7502.aspx">Azon</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 02/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>At least 4-5 years programming experience with <strong>Python</strong> <strong>Python</strong> AWS MySQL Git Java - We have partnered with an international, renewables focused, energy trading and services company to recruit for a Senior Software Developer for their Dublin or Letterkenny office.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8827160">Save This Job </a>
                                    <a class="show-more" jobId="8827160" href='/Jobs/Senior-Software-Developer-8827160.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8829297" href='/Jobs/Data-Analyst-8829297.aspx' >Data Analyst</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€96,000 - €120,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 05/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>SQL Tableau <strong>Python</strong> Hi all, A great opportunity has arisen to join a large Insurance firm based in Dublin. As a Data Analyst you will work with various departments to - Hi all, A great opportunity has arisen to join a large Insurance firm based in Dublin.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8829297">Save This Job </a>
                                    <a class="show-more" jobId="8829297" href='/Jobs/Data-Analyst-8829297.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Archer-Recruitment-3823.aspx"><img alt="Archer Recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/3823-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=ddbc9c173878827ef6f9c8979e1e657be26be46028c44cef9c15a6984d3022e5"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8828832" href='/Jobs/Software-Engineering-Manager-Limerick-8828832.aspx' >Software Engineering Manager - Limerick</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Archer-Recruitment-3823.aspx">Archer Recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 05/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Limerick/">Limerick</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Software engineering background with .Net, Java, <strong>Python</strong> or similar - Software Engineering Manager opportunity with a fast growing, successful technology company based in Limerick. In this role you will have great scope to grow in seniority – building and managing larger teams, and growing leaders underneath you.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8828832">Save This Job </a>
                                    <a class="show-more" jobId="8828832" href='/Jobs/Software-Engineering-Manager-Limerick-8828832.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/CareerWise-Recruitment-1718.aspx"><img alt="CareerWise Recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1718-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=c87b5ac393880e25a7dc6847620687a45b38d628060b202ce63c050cf95631ec"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8823652" href='/Jobs/Analytical-Recipe-Writer-BioTech-Remote-8823652.aspx' >Analytical Recipe Writer, BioTech (Remote, 12M)</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/CareerWise-Recruitment-1718.aspx">CareerWise Recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Familiarity with programming languages (e.g.: Java, <strong>Python,</strong> r, Regex, HTML) required. ANALYTICAL RECIPE WRITER required on a remote basis (to support technical work in the US) by out BioTech client in Cork. Initial 12 month contract on - Initial 12 month contract on offer.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8823652">Save This Job </a>
                                    <a class="show-more" jobId="8823652" href='/Jobs/Analytical-Recipe-Writer-BioTech-Remote-8823652.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8829212" href='/Jobs/QA-Test-Engineer-8829212.aspx' >QA Test Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€72,000 - €72,240 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 05/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Test Automation Java Selenium <strong>Python</strong> .NET C# Testing - Test Automation Engineer - 12 Month Contract I have an exciting opportunity for a Test Automation Engineer to join a client of mine. My client are - Test Automation Engineer - 12 Month Contract - I have an exciting opportunity for a Test Automation Engineer to join a client of mine.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8829212">Save This Job </a>
                                    <a class="show-more" jobId="8829212" href='/Jobs/QA-Test-Engineer-8829212.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Brightwater-959.aspx"><img alt="Brightwater" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/959-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=8317abc2d4322b9ff0429a4e9e612661cc4ef3c30cf51a8de1fbb5e3cd27bf82"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830554" href='/Jobs/Test-Automation-Architect-8830554.aspx' >Test Automation Architect</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Brightwater-959.aspx">Brightwater</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Coding (Java, Kotlin, C#, <strong>Python,</strong> Golang). 6 Month Daily Rate Contract - About the Company - My client are a leading blockchain technology company Headquartered in Dublin City Centre. They have had significant success in the blockchain space with products that bring their customers into the new age of digital global trade.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830554">Save This Job </a>
                                    <a class="show-more" jobId="8830554" href='/Jobs/Test-Automation-Architect-8830554.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Workday-7414.aspx"><img alt="Workday" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/7414-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7308a8f75f890791dd2dbe84b027303287555793ca684356bc2421e983de2745"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8824450" href='/Jobs/Junior-Software-Engineer-8824450.aspx' >Junior Software Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Workday-7414.aspx">Workday</a>
                                            </h3>
                                        
  <style data-styled="fLtnCS" data-styled-version="4.4.0">
/* sc-component-id: Star__StyledSvg-sc-1ge1c9k-0 */
.sky-component .fLtnCS{margin:0 1px;width:21px;height:21px;}</style>

  

  <div id="sky-65aace24e2b188e9-3" class="sky-component ZG9udXQ"><div><div class="sky-search-rating"><div class="sky-search-rating__stars"><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0qbbcb20jb5" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0qbbcb20jb5)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0pjvtlbtdyvj" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0pjvtlbtdyvj)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0vlut0svsg8" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0vlut0svsg8)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0etfls5a82o" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0etfls5a82o)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0v7ou71cbj3a" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="50%" style="stop-color:#f3d756"></stop><stop offset="50%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0v7ou71cbj3a)" stroke="#f3d756"></path></svg></div><div class="sky-search-rating__reviews-count">9<!-- --> company<!-- --> <!-- -->reviews</div></div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-3",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"7414","data":{"localId":"7414","surveysCount":9,"overallRatingAvg":4.37855,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Engineering experience using one or more of the following: Java, Scala, <strong>Python,</strong> Golang - Do what you love. Love what you do. At Workday, we help the world's largest organizations adapt to what's next by bringing finance, HR, and planning</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8824450">Save This Job </a>
                                    <a class="show-more" jobId="8824450" href='/Jobs/Junior-Software-Engineer-8824450.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Workday-7414.aspx"><img alt="Workday" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/7414-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7308a8f75f890791dd2dbe84b027303287555793ca684356bc2421e983de2745"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8828709" href='/Jobs/Principal-Senior-Software-Development-Engineer-8828709.aspx' >Principal/Senior Software Development Engineer - Distributed Systems</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Workday-7414.aspx">Workday</a>
                                            </h3>
                                        
  <style data-styled="fLtnCS" data-styled-version="4.4.0">
/* sc-component-id: Star__StyledSvg-sc-1ge1c9k-0 */
.sky-component .fLtnCS{margin:0 1px;width:21px;height:21px;}</style>

  

  <div id="sky-65aace24e2b188e9-3" class="sky-component ZG9udXQ"><div><div class="sky-search-rating"><div class="sky-search-rating__stars"><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0qbbcb20jb5" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0qbbcb20jb5)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0pjvtlbtdyvj" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0pjvtlbtdyvj)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0vlut0svsg8" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0vlut0svsg8)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0etfls5a82o" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0etfls5a82o)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0v7ou71cbj3a" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="50%" style="stop-color:#f3d756"></stop><stop offset="50%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0v7ou71cbj3a)" stroke="#f3d756"></path></svg></div><div class="sky-search-rating__reviews-count">9<!-- --> company<!-- --> <!-- -->reviews</div></div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-3",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"7414","data":{"localId":"7414","surveysCount":9,"overallRatingAvg":4.37855,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 04/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Must have strong coding skills (Java/<strong>Python/</strong>Go). Do what you love. Love what you do. At Workday, we help the world's largest organizations adapt to what's next by bringing finance, HR, and planning - At Workday, we help the world's largest organizations adapt to what's next by bringing finance, HR, and planning into a single enterprise cloud.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8828709">Save This Job </a>
                                    <a class="show-more" jobId="8828709" href='/Jobs/Principal-Senior-Software-Development-Engineer-8828709.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Life-Science-Consultants-3288.aspx"><img alt="Life Science Consultants" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/3288-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=bc1947bed6e45807c22e3f4ab39dc66f87db73e0c78abf13e70b2c04902d8068"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8822485" href='/Jobs/Technical-Scientist-Recipe-Writer-8822485.aspx' >Technical Scientist/Recipe Writer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Life-Science-Consultants-3288.aspx">Life Science Consultants</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 07/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Cork/">Cork</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Familiarity with programming languages (e.g.: Java, <strong>Python,</strong> r, Regex, HTML) LSC have a great contract opportunity for a Technical Scientist/Recipe Writer to join a leading biotech company based in Cork. If you have</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8822485">Save This Job </a>
                                    <a class="show-more" jobId="8822485" href='/Jobs/Technical-Scientist-Recipe-Writer-8822485.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/itContracting-5819.aspx"><img alt="itContracting" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5819-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=81e1d3d4b21488b361128c75d36a33b83c24bd1e43b9e7eb42df6e2b7edde8a0"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8823295" href='/Jobs/Senior-Data-Scientist-8823295.aspx' >Senior Data Scientist</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/itContracting-5819.aspx">itContracting</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span><strong>Python</strong> itContracting are currently seeking applicants for a Senior Data Scientist. This is a permanent position located with our client in Belfast (Hybrid - This is a permanent position located with our client in Belfast (Hybrid working available)</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8823295">Save This Job </a>
                                    <a class="show-more" jobId="8823295" href='/Jobs/Senior-Data-Scientist-8823295.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8818337" href='/Jobs/Senior-Software-Developer-8818337.aspx' >Senior Software Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€80,000 - €90,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 29/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Senior <strong>Python</strong> Developer <strong>Python</strong> | MySQL | AWS - A very successful software company who have just been acquired by a huge household name are looking for a Senior <strong>Python</strong> Developer to join them. You will have strong <strong>Python</strong> experience, anything else can be taught. * <strong>Python</strong> background <strong>Python</strong> AWS Software Developer <strong>Python</strong> Developer Ireland</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8818337">Save This Job </a>
                                    <a class="show-more" jobId="8818337" href='/Jobs/Senior-Software-Developer-8818337.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Frank-Recruitment-Group-13018.aspx"><img alt="Frank Recruitment Group" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/13018-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=373371cfc3144e13dddd3682bf4488e4a572f114bcf7da9df155dfb03e46f356"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8822668" href='/Jobs/Senior-AWS-DevOps-Engineer-8822668.aspx' >Senior AWS DevOps Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Frank-Recruitment-Group-13018.aspx">Frank Recruitment Group</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€57,000 - €96,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 07/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Background in Java, Powershell or <strong>Python,</strong> Windows, Linux, Ruby - As a Senior DevOps Engineer you will play an important role in building DevOps CI/CD platforms, and implementing coding framework in order to reinforce core products. You will be supporting the Solution Architect in the construction of platforms and frameworks related to DevOps culture.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8822668">Save This Job </a>
                                    <a class="show-more" jobId="8822668" href='/Jobs/Senior-AWS-DevOps-Engineer-8822668.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Zenith-Technologies-1903.aspx"><img alt="Zenith Technologies" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1903-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=dbfdf0006a8680859cb6bce6d1bad33f22068adfcc29200571d4a71d6155c4fe"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8828566" href='/Jobs/MES-Program-Project-Manager-8828566.aspx' >MES Program/Project Manager</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Zenith-Technologies-1903.aspx">Zenith Technologies</a>
                                            </h3>
                                        
  <style data-styled="" data-styled-version="4.4.0"></style>

  

  <div id="sky-65aace24e2b188e9-8" class="sky-component ZG9udXQ"><div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-8",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"1903","data":{"localId":"1903","surveysCount":11,"overallRatingAvg":2.78719,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Cork/">Cork</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Knowledge of coding using C#, <strong>python</strong> etc is a plus - Zenith Technologies, now a Cognizant Company is a world leader in delivering digital transformation solutions to Life Sciences. Through our knowledge</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8828566">Save This Job </a>
                                    <a class="show-more" jobId="8828566" href='/Jobs/MES-Program-Project-Manager-8828566.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8821640" href='/Jobs/Data-Analyst-8821640.aspx' >Data Analyst</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€49,000 - €60,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 05/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Data Analyst Salary: €49,000-€60,000 DOE A client of mine, a growing start up, has decided to expand their team further. They are currently working</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8821640">Save This Job </a>
                                    <a class="show-more" jobId="8821640" href='/Jobs/Data-Analyst-8821640.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8823656" href='/Jobs/Full-Stack-NET-Engineer-8823656.aspx' >Full Stack .NET Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€50,000 - €60,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>· Experience with Angular, React, VueJS, NodeJs, Azure, AWS, Google Cloud, MicroServices, Docker, Kubernetes, Kafka, Redis, DevOps, Test Automation, <strong>Python,</strong> Git - Full-Stack C# / .NET Developer Salary: €40,000 - €70,000 Remote Working (Within Ireland) I'm working with an extremely cutting edge and rapidly - Full-Stack C# / .NET Developer - Salary: €40,000 - €70,000 - Remote Working (Within Ireland)</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8823656">Save This Job </a>
                                    <a class="show-more" jobId="8823656" href='/Jobs/Full-Stack-NET-Engineer-8823656.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/The-Ardonagh-Group-14608.aspx"><img alt="The Ardonagh Group" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/14608-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=f31787175b91528b1ea8159e06359a3dd8ea49dedda3d518ba745096943a449f"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830980" href='/Jobs/Data-Engineer-8830980.aspx' >Data Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/The-Ardonagh-Group-14608.aspx">The Ardonagh Group</a>
                                            </h3>
                                        
                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Westmeath/">Westmeath</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Strong command of relevant programming/scripting languages: e.g., Java, Scala, <strong>Python,</strong> R. The Ardonagh Analytics Lab, based in Mullingar, Ireland, delivers unrivalled risk insight and innovative data-driven solutions for The Ardonagh Group’s collective of leading businesses, their customers and insurance partners.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830980">Save This Job </a>
                                    <a class="show-more" jobId="8830980" href='/Jobs/Data-Engineer-8830980.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Stelfox-1626.aspx"><img alt="Stelfox" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1626-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=fca5c0061a2933f5e18cd12757f055bf8c9efbd2d158f007ab14c7c09dc4ee6b"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830580" href='/Jobs/Cassandra-Database-Administrator-8830580.aspx' >Cassandra Database Administrator</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Stelfox-1626.aspx">Stelfox</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Working on automating existing system monitoring/creating dashboard using Shell script, <strong>Python.</strong> My client, a Multi-national corporation is looking to hire a Cassandra DBA on an initial 12 month contract with a view to extending.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830580">Save This Job </a>
                                    <a class="show-more" jobId="8830580" href='/Jobs/Cassandra-Database-Administrator-8830580.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8826238" href='/Jobs/Senior-Big-Data-Engineer-8826238.aspx' >Senior Big Data Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€100,000 - €120,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 29/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Background in Scala, <strong>Python</strong> or PyTorch - This We're working closely with a global advertising company who have ambitious plans to expand their IT presence in Ireland. This company is a leading provider of cutting-edge solutions, services and content and they are the current trend setters within their industry.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8826238">Save This Job </a>
                                    <a class="show-more" jobId="8826238" href='/Jobs/Senior-Big-Data-Engineer-8826238.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/REALTIME-recruitment-3053.aspx"><img alt="REALTIME recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/3053-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=af8b091bd6d65059f23b9006acfb7306dd1f677bed0d5fcb8e76d4057358b8e3"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8816914" href='/Jobs/Senior-Data-Engineer-with-AWS-8816914.aspx' >Senior Data Engineer with AWS/Snowflake)</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/REALTIME-recruitment-3053.aspx">REALTIME recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€60,000 - €80,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 27/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>3 years' <strong>Python</strong>-Powershell, API's (rest-soap), ETL pipelines Redshift, Snowflake, BigQuery etc...) Senior Data Engineer (Fully Remote Role-Unlimited Annual Leave) Multinational client with a presence in North America, UK and Ireland looking for - Senior Data Engineer (Fully Remote Role-Unlimited Annual Leave)</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8816914">Save This Job </a>
                                    <a class="show-more" jobId="8816914" href='/Jobs/Senior-Data-Engineer-with-AWS-8816914.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Osborne-1755.aspx"><img alt="Osborne" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1755-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=ae6e6131f84211fdf8e36ccd812f72e52aeea57bbd3327455a5e809f741bf832"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8828270" href='/Jobs/Senior-Backend-Developer-DevOps-Engineer-8828270.aspx' >Senior Backend Developer/DevOps Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Osborne-1755.aspx">Osborne</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 04/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
<span>&nbsp;/</span>                                                <a href="/Jobs/Dublin-North/">Dublin North</a>
<span>&nbsp;/</span>                                                <a href="/Jobs/Dublin-City-Centre/">Dublin City Centre</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>· 6+ years of professional programming experience, 3 years using Back end programming languages (e.g. RoR, <strong>Python,</strong> NodeJS, Java) Osborne is looking for a Senior Backend / DevOps Engineer to join our client – a global leader in aeronautics, space and related services.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8828270">Save This Job </a>
                                    <a class="show-more" jobId="8828270" href='/Jobs/Senior-Backend-Developer-DevOps-Engineer-8828270.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Workday-7414.aspx"><img alt="Workday" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/7414-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7308a8f75f890791dd2dbe84b027303287555793ca684356bc2421e983de2745"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8821673" href='/Jobs/Software-Engineer-Service-Mesh-8821673.aspx' >Software Engineer - Service Mesh</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Workday-7414.aspx">Workday</a>
                                            </h3>
                                        
  <style data-styled="fLtnCS" data-styled-version="4.4.0">
/* sc-component-id: Star__StyledSvg-sc-1ge1c9k-0 */
.sky-component .fLtnCS{margin:0 1px;width:21px;height:21px;}</style>

  

  <div id="sky-65aace24e2b188e9-3" class="sky-component ZG9udXQ"><div><div class="sky-search-rating"><div class="sky-search-rating__stars"><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0qbbcb20jb5" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0qbbcb20jb5)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0pjvtlbtdyvj" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0pjvtlbtdyvj)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0vlut0svsg8" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0vlut0svsg8)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0etfls5a82o" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="100%" style="stop-color:#f3d756"></stop><stop offset="100%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0etfls5a82o)" stroke="#f3d756"></path></svg><svg height="21px" width="21px" viewBox="0 0 267.235 255.176" class="Star__StyledSvg-sc-1ge1c9k-0 fLtnCS"><defs><linearGradient id="starGradient0v7ou71cbj3a" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="50%" style="stop-color:#f3d756"></stop><stop offset="50%" style="stop-color:#f2f2f2"></stop></linearGradient></defs><path d="M252.93 87.3l-71.68-6.779c-4.512-.411-8.413-3.279-10.268-7.601l-25.67-62.22c-4.103-10.268-18.683-10.268-22.793 0L97.05 72.92c-1.635 4.322-5.746 7.189-10.269 7.601L15.121 87.3C4.441 88.323.129 101.679 8.142 108.859l54.01 47.44c3.489 3.091 4.923 7.604 3.9 12.13l-16.224 66.53c-2.467 10.479 8.834 19.1 18.28 13.559l59.753-35.12c3.91-2.267 8.634-2.267 12.535 0l59.752 35.12c9.456 5.541 20.747-2.879 18.28-13.559l-16.01-66.53c-1.033-4.521.411-9.03 3.896-12.13l54.01-47.44c7.79-7.18 3.28-20.536-7.4-21.559z" fill="url(#starGradient0v7ou71cbj3a)" stroke="#f3d756"></path></svg></div><div class="sky-search-rating__reviews-count">9<!-- --> company<!-- --> <!-- -->reviews</div></div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-3",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"7414","data":{"localId":"7414","surveysCount":9,"overallRatingAvg":4.37855,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 04/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Proficient in at least one of the following languages: Ruby, Go, or <strong>Python.</strong> Do what you love. Love what you do. At Workday, we help the world's largest organizations adapt to what's next by bringing finance, HR, and planning</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8821673">Save This Job </a>
                                    <a class="show-more" jobId="8821673" href='/Jobs/Software-Engineer-Service-Mesh-8821673.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Genesys-13622.aspx"><img alt="Genesys" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/13622-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=bf08d5aa9650661b4166bbc48b8b7e92e7524c59da8bbc23629e852caf771e7f"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8826084" href='/Jobs/Full-Stack-Engineer-8826084.aspx' >Full Stack Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Genesys-13622.aspx">Genesys</a>
                                            </h3>
                                        
                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 06/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Galway/">Galway</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>You have some experience in either <strong>Python,</strong> Java, or JavaScript. * You have contributed to enterprise grade applications in either <strong>Python,</strong> Java or JavaScript - Great customer experiences start with Genesys. Through its market leading cloud contact center solution, Genesys Cloud CX, Genesys unifies customer</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8826084">Save This Job </a>
                                    <a class="show-more" jobId="8826084" href='/Jobs/Full-Stack-Engineer-8826084.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8817762" href='/Jobs/Senior-Data-Engineer-8817762.aspx' >Senior Data Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€90,000 - €110,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 29/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Programming experience in <strong>Python</strong> and/or Java - This We're working exclusively with a global multimedia company who have ambitious plans to expand their IT presence in Ireland. This company is a leading provider of cutting-edge solutions, services and content and they are the current trend setters within their industry</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8817762">Save This Job </a>
                                    <a class="show-more" jobId="8817762" href='/Jobs/Senior-Data-Engineer-8817762.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/FRS-Recruitment-1499.aspx"><img alt="FRS Recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1499-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=bbb7f79ea9bf6831d94a151b1e37a9bb1c1da24e3eca144badb5e828b327ac3f"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8817312" href='/Jobs/Senior-Data-Engineer-Financial-Sector-8817312.aspx' >Senior Data Engineer | Financial Sector | Dublin, Hybrid</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/FRS-Recruitment-1499.aspx">FRS Recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 28/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Data-orchestration experience using SSIS, <strong>Python,</strong> Powershell, Snowpipe or equivalent. Senior Data Engineer | Hybrid, Dublin A global financial management and asset advisory firm is now welcoming applications for the exciting role of - Senior Data Engineer | Hybrid, Dublin</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8817312">Save This Job </a>
                                    <a class="show-more" jobId="8817312" href='/Jobs/Senior-Data-Engineer-Financial-Sector-8817312.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Xilinx-part-of-AMD-6907.aspx"><img alt="Xilinx part of AMD" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/6907-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=4ee39ea72eeb016c4a80a7fe75f68ea086d1517f1c2591b1738ae2f10393ea7e"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8823494" href='/Jobs/Lead-Verification-Engineer-8823494.aspx' >Lead Verification Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Xilinx-part-of-AMD-6907.aspx">Xilinx part of AMD</a>
                                            </h3>
                                        
  <style data-styled="" data-styled-version="4.4.0"></style>

  

  <div id="sky-65aace24e2b188e9-5" class="sky-component ZG9udXQ"><div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-5",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"6907","data":{"localId":"6907","surveysCount":7,"overallRatingAvg":2.69086,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Belfast/">Belfast</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Experience with scripting languages: <strong>Python,</strong> Tcl, Perl preferred - What you do at AMD changes everything At AMD, we push the boundaries of what is possible. We believe in changing the world for the better by driving - What you do at AMD changes everything - At AMD, we push the boundaries of what is possible.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8823494">Save This Job </a>
                                    <a class="show-more" jobId="8823494" href='/Jobs/Lead-Verification-Engineer-8823494.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Xilinx-part-of-AMD-6907.aspx"><img alt="Xilinx part of AMD" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/6907-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=4ee39ea72eeb016c4a80a7fe75f68ea086d1517f1c2591b1738ae2f10393ea7e"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8823492" href='/Jobs/Lead-Design-Engineer-8823492.aspx' >Lead Design Engineer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Xilinx-part-of-AMD-6907.aspx">Xilinx part of AMD</a>
                                            </h3>
                                        
  <style data-styled="" data-styled-version="4.4.0"></style>

  

  <div id="sky-65aace24e2b188e9-5" class="sky-component ZG9udXQ"><div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-5",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"6907","data":{"localId":"6907","surveysCount":7,"overallRatingAvg":2.69086,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 09/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Belfast/">Belfast</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Experience with scripting languages: <strong>Python,</strong> Tcl, Perl preferred - What you do at AMD changes everything At AMD, we push the boundaries of what is possible. We believe in changing the world for the better by driving - What you do at AMD changes everything - At AMD, we push the boundaries of what is possible.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8823492">Save This Job </a>
                                    <a class="show-more" jobId="8823492" href='/Jobs/Lead-Design-Engineer-8823492.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Stelfox-1626.aspx"><img alt="Stelfox" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1626-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=fca5c0061a2933f5e18cd12757f055bf8c9efbd2d158f007ab14c7c09dc4ee6b"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8818598" href='/Jobs/Senior-Cloud-Developer-8818598.aspx' >Senior Cloud Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Stelfox-1626.aspx">Stelfox</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 30/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Dublin/">Dublin</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Strong experience with Core Java, <strong>Python</strong> (and frameworks). We are looking for an experienced Cloud Developer to join a Cloud Platforms based project with one of our clients based in a Global organisation operating in the Financial services sphere.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8818598">Save This Job </a>
                                    <a class="show-more" jobId="8818598" href='/Jobs/Senior-Cloud-Developer-8818598.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/FRS-Recruitment-1499.aspx"><img alt="FRS Recruitment" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/1499-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=bbb7f79ea9bf6831d94a151b1e37a9bb1c1da24e3eca144badb5e828b327ac3f"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8821793" href='/Jobs/Senior-Machine-Learning-Engineer-World-8821793.aspx' >Senior Machine Learning Engineer - World Class Tech Company</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/FRS-Recruitment-1499.aspx">FRS Recruitment</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 06/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Limerick/">Limerick</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Solid <strong>Python</strong> programming language skills - Machine Learning AI Edge Technologies Data Science <strong>Python</strong> You will join a high-performing team developing leading-edge ML technologies running on advanced edge AI devices A world-class tech company that</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8821793">Save This Job </a>
                                    <a class="show-more" jobId="8821793" href='/Jobs/Senior-Machine-Learning-Engineer-World-8821793.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/The-Ardonagh-Group-14608.aspx"><img alt="The Ardonagh Group" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/14608-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=f31787175b91528b1ea8159e06359a3dd8ea49dedda3d518ba745096943a449f"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8830977" href='/Jobs/Senior-Data-Architect-8830977.aspx' >Senior Data Architect</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/The-Ardonagh-Group-14608.aspx">The Ardonagh Group</a>
                                            </h3>
                                        
                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Westmeath/">Westmeath</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Knowledgeable with ETL technologies such as SSIS, <strong>Python.</strong> ETL technologies MS SQL SSIS <strong>Python</strong> PowerBI Tableau Qlikview - The Ardonagh Analytics Lab, based in Mullingar, Ireland, delivers unrivalled risk insight and innovative data-driven solutions for The Ardonagh Group’s collective of leading businesses, their customers and insurance partners.</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8830977">Save This Job </a>
                                    <a class="show-more" jobId="8830977" href='/Jobs/Senior-Data-Architect-8830977.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Genesys-13622.aspx"><img alt="Genesys" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/13622-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=bf08d5aa9650661b4166bbc48b8b7e92e7524c59da8bbc23629e852caf771e7f"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8826411" href='/Jobs/Software-Engineer-DevOps-Mid-Senior-8826411.aspx' >Software Engineer, DevOps (Mid/Senior)</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Genesys-13622.aspx">Genesys</a>
                                            </h3>
                                        
                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 07/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Nationwide/">Nationwide</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>You will need to have a solid understanding of Java and/or <strong>Python,</strong> REST API solutions and application development. * Firm understanding of backend application development using <strong>Python,</strong> Java, REST API and NoSQL solutions. * Experience with <strong>Python</strong> or Java</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8826411">Save This Job </a>
                                    <a class="show-more" jobId="8826411" href='/Jobs/Software-Engineer-DevOps-Mid-Senior-8826411.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Fiserv-4535.aspx"><img alt="Fiserv" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/4535-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7701491c17528b5a548fbeff41e32f9b8e3993a5b36c9e32cb6fa50bd35dad28"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8827128" href='/Jobs/DevOps-Engineering-Lead-8827128.aspx' >DevOps Engineering Lead</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Fiserv-4535.aspx">Fiserv</a>
                                            </h3>
                                        
  <style data-styled="" data-styled-version="4.4.0"></style>

  

  <div id="sky-65aace24e2b188e9-11" class="sky-component ZG9udXQ"><div></div></div>

  <script type="text/javascript">
    (function () {
      function loadBundle(e,t,d){var a=window.__skylight__,i=document.getElementsByTagName("head")[0],o=d+"/all.js?_="+t,n=function(){for(var e=0;e<a.loadQueue.length;e++)loadWidget(a.loadQueue[e])};a.scriptLoading=!0;var l=document.createElement("script");l.setAttribute("type","text/javascript"),l.setAttribute("src",o),l.onload=n,i.appendChild(l)}function loadWidget(e){var t=window.__skylight__;if("function"==typeof t.getWidget){var d=document.getElementById(e.elementId);t.getWidget(e.name).renderClient(d,e.data)}else t.loadQueue.indexOf(e)<0&&t.loadQueue.push(e),t.scriptLoading||loadBundle(e.data.jobSiteId,e.cacheParam,e.serverHost)}"object"!=typeof window.__skylight__&&(window.__skylight__={loadQueue:[],scriptLoading:!1,loadWidget:loadWidget});
      window.__skylight__.loadWidget({ name: "company_rating_summary", elementId: "sky-65aace24e2b188e9-11",
        data: {"componentTemplate":"search","apiVersion":"v2","companyId":"4535","data":{"localId":"4535","surveysCount":6,"overallRatingAvg":2.48723,"linkType":"COMPANY_REVIEW_PAGE"},"jobSiteId":"irishjobs.ie","urlTemplates":{},"assetsBaseUrl":"\/skylight-ui\/static\/assets","lang":"en"}, cacheParam: "97ee331", serverHost: "/skylight-ui/static"})
    }());
  </script>

                                    </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">Not disclosed</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 10/08/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Tipperary/">Tipperary</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span>Scripting Skills: Strong scripting (e.g. <strong>Python,</strong> bash or PowerShell) and automation skills - DevOps Lead Project Overview The Fiserv Analytics team develop data driven applications that deliver business insights and data visualisations to both - DevOps Lead - Project Overview</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8827128">Save This Job </a>
                                    <a class="show-more" jobId="8827128" href='/Jobs/DevOps-Engineering-Lead-8827128.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>
                        <div class="module job-result  ">
                            <div class="module-content">
                                <div class="job-result-logo-title">
                                    <div class="job-result-toggle" style="display: block;">
                                        <span class="not-for-me" >Not for me</span>
                                    </div>
                                        <div class="job-result-logo">
                                                <a href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx"><img alt="Reperio Human Capital Ltd" src="https://irishjobs-web-prd.s3.eu-west-1.amazonaws.com/assets/employer-logos/5979-small.gif?X-Amz-Expires=86400&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA3UBW7IFPIFTBQVKM/20220810/eu-west-1/s3/aws4_request&amp;X-Amz-Date=20220810T200834Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=33eb341eb52f36637336ea7ffc9de124e4461ea593e6161e6dc46352d5c5e3fd"></a>
                                        </div>
                                    <div class="job-result-title">

                                        <h2 itemprop="title">
                                            <a jobId="8825043" href='/Jobs/Senior-Software-Developer-8825043.aspx' >Senior Software Developer</a>
                                        </h2>
                                            <h3 itemprop="name">
                                                    <a itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization" href="/Recruiters/Reperio-Human-Capital-Ltd-5979.aspx">Reperio Human Capital Ltd</a>
                                            </h3>
                                                                            </div>
                                </div>
                                <div class="job-result-overview" style="display: ">
                                    <ul class="job-overview job-overview-list">
                                        <li itemprop="baseSalary" class="salary">€80,000 - €90,000 per annum</li>
                                        <li itemprop="datePosted" class="updated-time">Updated 27/07/2022</li>
                                        <li itemprop="jobLocation" class="location">
                                                <a href="/Jobs/Working-from-Home/">Working from Home</a>
                                        </li>
                                    </ul>
                                </div>
                                <p itemprop="description" style="display: ">
                                        <span><strong>Python</strong> | MySQL | AWS | CI/CD | Ireland | Dublin | Hybrid - They are looking to grow their team and as such, are looking for a Senior <strong>Python</strong> Developer to join them on a permanent, FT basis. * <strong>Python</strong> 4+years <strong>Python</strong> MySQL Backend Developer AWS Dublin Software - Permanent Full-Time - Job Description</span>
                                </p>
                                <div class="job-result-cta" style="display: ">
                                    <a class="save-job" style="cursor: pointer; background-color: #ffffff; color: #cad466; background-image: url('/img/icons/star-green-small.png');" jobId="8825043">Save This Job </a>
                                    <a class="show-more" jobId="8825043" href='/Jobs/Senior-Software-Developer-8825043.aspx'>Show More</a>
                                </div>
                            </div>
                        </div>

                    <ul id="pagination">
        
                      <li><a rel="nofollow" class="active">1</a></li>
        
                
    </ul>


                    <div class="duplicate-megssage">
                        In order to show you the most relevant results, we have omitted some entries very similar to the 285 already displayed. If necessary, you can <a rel='nofollow' href='https://www.irishjobs.ie/ShowResults.aspx?Keywords=python&amp;PerPage=500&amp;dup=on'>repeat the search with the omitted results included.</a>
                    </div>
                    <div class="faq-card">

        <script type="application/ld+json">{
  "@context": "https://schema.org/",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How to hire python staff in Ireland?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can <a href=\"https://www.irishjobs.ie/recruiters/?key=Python\">hire for python jobs on IrishJobs.ie</a>. Find your ideal employees. Start today."
      }
    },
    {
      "@type": "Question",
      "name": "Which jobs similar to python are in demand?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "There is high demand for <a href='https://www.irishjobs.ie/Software-Jobs'>Software</a>, <a href='https://www.irishjobs.ie/Big-Data-Jobs'>Big Data</a> and <a href='https://www.irishjobs.ie/Data-Engineer-Jobs'>Data Engineer</a> jobs."
      }
    },
    {
      "@type": "Question",
      "name": "How many python jobs are available on IrishJobs.ie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "There are 285 python jobs available on <a href=\"https://www.irishjobs.ie\">IrishJobs.ie</a>."
      }
    },
    {
      "@type": "Question",
      "name": "What cities have the most python jobs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<a href='https://www.irishjobs.ie/Python-Jobs-in-Laois'>Laois</a>, <a href='https://www.irishjobs.ie/Python-Jobs-in-Longford'>Longford</a> and <a href='https://www.irishjobs.ie/Python-Jobs-in-Offaly'>Offaly</a> are the top cities with python jobs in Ireland."
      }
    }
  ]
}</script>
        <div class="card-header">
            <h4>Frequently Asked Questions</h4>
        </div>
        <ul>
                <li>
                    <span class="question">How to hire python staff in Ireland?</span>
                    <span class="answer">You can <a href="https://www.irishjobs.ie/recruiters/?key=Python">hire for python jobs on IrishJobs.ie</a>. Find your ideal employees. Start today.</span>
                </li>
                <li>
                    <span class="question">Which jobs similar to python are in demand?</span>
                    <span class="answer">There is high demand for <a href='https://www.irishjobs.ie/Software-Jobs'>Software</a>, <a href='https://www.irishjobs.ie/Big-Data-Jobs'>Big Data</a> and <a href='https://www.irishjobs.ie/Data-Engineer-Jobs'>Data Engineer</a> jobs.</span>
                </li>
                <li>
                    <span class="question">How many python jobs are available on IrishJobs.ie?</span>
                    <span class="answer">There are 285 python jobs available on <a href="https://www.irishjobs.ie">IrishJobs.ie</a>.</span>
                </li>
                <li>
                    <span class="question">What cities have the most python jobs?</span>
                    <span class="answer"><a href='https://www.irishjobs.ie/Python-Jobs-in-Laois'>Laois</a>, <a href='https://www.irishjobs.ie/Python-Jobs-in-Longford'>Longford</a> and <a href='https://www.irishjobs.ie/Python-Jobs-in-Offaly'>Offaly</a> are the top cities with python jobs in Ireland.</span>
                </li>
        </ul>
    </div>

            </div>
        </div>
    </div>

</div>



    
<footer id="global-footer">
    <div class="productVersion" style="width: 90%; height: 40px; background-color: white; margin:auto; padding: 10px; display: none;">
        Environment: www.irishjobs.ie, Build Version: V 1.0.1.0, Date Release: 04/04/2017
    </div>
    <div class="container">

        <div class="footer-column5">
            <h4>Learn More</h4>
            <ul>
                <li><a href='https://www.irishjobs.ie/careeradvice/irishjobs-ie-user-guides/'>Jobseeker Help Guides</a></li>
                <li><a href='https://www.irishjobs.ie/careeradvice/newsroom/'>Newsroom</a></li>
                <li><a href='/about/contact'>Contact Us</a></li>
            </ul>
        </div>

        <div class="footer-column5">
            <h4>&nbsp;</h4>
            <ul>
                <li><a href='/Recruiters/Saongroup-com-3233.aspx'>Careers</a></li>
                <li><a href='/about/privacy'>Privacy Policy</a></li>
                <li><a href='/about/international'>Partner Sites</a></li>
                <li>&nbsp;</li>
            </ul>
        </div>

        <div class="footer-column5">
            <h4>About Us</h4>
            <ul>
                <li><a href='/about'>About Us</a></li>
                <li><a href='/about/terms'>Terms of Use</a></li>
                <li><a href='/about/cookie-policy'>Cookie Policy</a></li>
            </ul>
        </div>

        <div class="footer-column5">
            <h4>Recruiters</h4>
            <ul>
                <li><a href="/recruiters/">Advertise A Job</a></li>
                <li><a href="/recruiters/international-sales/">Recruit Internationally</a></li>
                <li><a href='https://www.irishjobs.ie/recruiters/become-our-partner/'>Become Our Partner</a></li>
                <li><a href='https://hub.irishjobs.ie'>Recruiter Login </a></li>
            </ul>
        </div>

        <div class="footer-column connect-with-us">
            <h4>Connect with Us</h4>
            <div class="social-icons">
                <ul>
                    <li><a href="https://twitter.com/Irishjobsie" rel="nofollow" target="_blank" title='find us on twitter'><i class="fab fa-twitter-square" aria-hidden="true"></i></a></li>
                    <li><a href="https://www.facebook.com/irishjobs.ie" rel="nofollow" target="_blank" title='find us on facebook'><i class="fab fa-facebook-square" aria-hidden="true"></i></a></li>
                    <li><a href="https://www.instagram.com/irishjobsie/ " rel="nofollow" target="_blank" title='find us on instagram'><i class="fab fa-instagram" aria-hidden="true"></i></a></li>
                </ul>
            </div> 
        </div>

        <div class="clear"></div>

        <div style="text-align: center; color: #777777; border-top: 1px solid #222; margin-top: 5px; padding-top: 10px;">
            <p>
                &copy; 2022 IrishJobs.ie Registered in Ireland under Company Number 260762
            </p>
        </div>

    </div>

    <div id="app-footer">


        <div id="app-links">
            <!-- *** Replace download links once available *** -->
            <a href="https://app.adjust.com/j8zfif" target="_blank"><img src='/img/logos/googe-play-button.png' alt="Download the IrishJobs.ie app from Google Play" /></a>
            <p>
                download the app
            </p>            
            <a href="https://app.adjust.com/hjp4j3" target="_blank"><img src='/img/logos/app-store-button.png' alt="Download the IrishJobs.ie app from the App Store" /></a>            
        </div>

    </div>

</footer>

<script src="/bundles/js/cosmeticshelper-js?v=tdsrofVa1ZmdMbxVuj1VQ-ioqwsMi8iuPynkZNEduu01"></script>



    <script src="/bundles/js/SmartBanner?v=Q8m76nHb98SBniMu3xOscjtH5XdC5OqfyQfPSuupoQ41"></script>

        <script type="text/javascript">
        $(function () {
            $.smartbanner({
                price: 'GET', // Price of the app
                author: 'Saongroup Ltd.',
                //appStoreLanguage: 'us', // Language code for App Store
                inAppStore: 'On the App Store', // Text of price for iOS
                inGooglePlay: 'In Google Play', // Text of price for Android
                daysHidden: 7,
                daysReminder: 7,
                title: 'IrishJobs.ie Job Search',/*,
                                                                                                                                                force:'android'*/
                iconGloss: false // no gloss on ios icon
            });
        });
    </script>


    <script type="text/javascript">
        try {
            _satellite.pageBottom();
        } catch (e) {
        }
    </script>
    <!--Before Final MDB files-->
    
    

    <!--After Final MDB files-->

<script type="text/javascript"  src="/7u-RcK/J/9/4pF4AqHz8w/c3QipQhVaV/WxdmbgE/IQ/ZtJRMlF3U"></script></body>

<script type="text/javascript">
 
    function optsInOutTrack(statusName) {
        try {
            if (statusName.toString().toLowerCase() === 'true')
                _satellite.track("setprofilepublic");
            else
                _satellite.track("setprofileprivate");
        } catch (e) { }
    }

    // Click in menu or login/profile
    function showHideMenu(nameMenu) {
        let profileMenu = document.getElementById("profile-menu")
        let mainMenu = document.getElementById("main-menu")
        if (nameMenu === "profile") {

            mainMenu.classList.contains("show-menu") && mainMenu.classList.remove("show-menu")

            if (profileMenu.classList.contains("show-menu")) {
                profileMenu.classList.remove("show-menu")
            } else {
                profileMenu.classList.add("show-menu")
            }
        }
        else if (nameMenu === "main") {
            profileMenu.classList.contains("show-menu") && profileMenu.classList.remove("show-menu")

            if (mainMenu.classList.contains("show-menu")) {
                mainMenu.classList.remove("show-menu")
            } else {
                mainMenu.classList.add("show-menu")
            }
        }

    }

    function handleClickOutside() {
        let profileMenu = document.getElementById("profile-menu")
        let mainMenu = document.getElementById("main-menu")
        if ($(window).width() <= 766) {
            $(document).click(function (event) {
                var $target = $(event.target);
                if (!$target.closest("#main-menu").length && !$target.closest('#profile-menu').length && !$target.closest('.opc-mobile').length) {
                    if (profileMenu.classList.contains("show-menu")) {
                        profileMenu.classList.remove("show-menu")
                    }
                    if (mainMenu.classList.contains("show-menu")) {
                        mainMenu.classList.remove("show-menu")
                    }
                }
            })
        }
    }

    handleClickOutside()

</script>



<!-- This is a test string Main -->
</html>

"""

tree = html.fromstring(c)
job_pages = ['https://www.irishjobs.ie/'+p for p in tree.xpath('//div[@class="job-result-cta"]/a[2]/@href')]





JOB_REQUESTS_PATH = 'job-requests.p'

if os.path.exists(JOB_REQUESTS_PATH):
    job_requests = pickle.load(open(JOB_REQUESTS_PATH,"rb"))
else:
    job_requests = {}

skills_count = []

for p in job_pages:
    if p not in job_requests:
        page = requests.get(p)
        job_requests[p] = page
    else:
        page = job_requests[p]

    tree = html.fromstring(page.content)
    skills = tree.xpath('//span[@class="job-skills-pills"]/text()')
    print(skills)
    skills_count.extend(skills)

print(Counter(skills_count))


pickle.dump(job_requests, open(JOB_REQUESTS_PATH,"wb"))
