/**
 * author Remy Sharp
 * url http://remysharp.com/2009/01/26/element-in-view-event-plugin/
 * fork https://github.com/zuk/jquery.inview
 */
(function($) {
    'use strict';

    function getScrollTop() {
        return window.pageYOffset ||
            document.documentElement.scrollTop ||
            document.body.scrollTop;
    }

    function getViewportHeight() {
        var height = window.innerHeight; // Safari, Opera
        // if this is correct then return it. iPad has compat Mode, so will
        // go into check clientHeight (which has the wrong value).
        if (height) {
            return height;
        }
        var mode = document.compatMode;

        if ((mode || !$.support.boxModel)) { // IE, Gecko
            height = (mode === 'CSS1Compat') ?
                document.documentElement.clientHeight : // Standards
                document.body.clientHeight; // Quirks
        }

        return height;
    }

    function offsetTop(debug) {
        // Manually calculate offset rather than using jQuery's offset
        // This works-around iOS < 4 on iPad giving incorrect value
        // cf http://bugs.jquery.com/ticket/6446#comment:9
        var curtop = 0;
        for (var obj = debug; obj; obj = obj.offsetParent) {
            curtop += obj.offsetTop;
        }
        return curtop;
    }

    function checkInView() {
        var viewportTop = getScrollTop(),
            viewportBottom = viewportTop + getViewportHeight(),
            elems = [];

        // naughty, but this is how it knows which elements to check for
        $.each($.cache, function() {
            if (this.events && this.events.inview) {
                elems.push(this.handle.elem);
            }
        });

        $(elems).each(function() {
            var $el = $(this),
                elTop = offsetTop(this),
                elHeight = $el.height(),
                elBottom = elTop + elHeight,
                wasInView = $el.data('inview') || false,
                offset = $el.data('offset') || 0,
                inView = elTop > viewportTop && elBottom < viewportBottom,
                isBottomVisible = elBottom + offset > viewportTop && elTop < viewportTop,
                isTopVisible = elTop - offset < viewportBottom && elBottom > viewportBottom,
                inViewWithOffset = inView || isBottomVisible || isTopVisible ||
                    (elTop < viewportTop && elBottom > viewportBottom);

            if (inViewWithOffset) {
                var visPart = (isTopVisible) ? 'top' : (isBottomVisible) ? 'bottom' : 'both';
                if (!wasInView || wasInView !== visPart) {
                    $el.data('inview', visPart);
                    $el.trigger('inview', [true, visPart]);
                }
            } else if (!inView && wasInView) {
                $el.data('inview', false);
                $el.trigger('inview', [false]);
            }
        });
    }

    function createFunctionLimitedToOneExecutionPerDelay(fn, delay) {
        var shouldRun = false;
        var timer = null;

        function runOncePerDelay() {
            if (timer !== null) {
                shouldRun = true;
                return;
            }
            shouldRun = false;
            fn();
            timer = setTimeout(function() {
                timer = null;
                if (shouldRun) {
                    runOncePerDelay();
                }
            }, delay);
        }

        return runOncePerDelay;
    }

    // ready.inview kicks the event to pick up any elements already in view.
    // note however, this only works if the plugin is included after the elements are bound to 'inview'
    var runner = createFunctionLimitedToOneExecutionPerDelay(checkInView, 100);
    $(window).on('checkInView.inview click.inview ready.inview scroll.inview resize.inview', runner);

})(jQuery);

/* Maps Plugin */
jQuery.fn.googleMap = function(options) {
  var settings = jQuery.extend({
    center: new google.maps.LatLng(37.208242, -93.295756),
    map_type: google.maps.MapTypeId.ROADMAP,
    markers: false,
    zoom: 12,
    recenter : false
  }, options);

  this.each(function() {
    var styles = [
      {
        "stylers": [
          { "saturation": -50 }
        ]
      },{
      }
    ];
    var styledMap = new google.maps.StyledMapType(styles, {name: "Styled Map"});
    var mapOptions = {
      mapTypeControlOptions: {
        mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
      }
    };
    var map = new google.maps.Map(this, {
      center : settings.center,
      disableDefaultUI : true,
      mapTypeId: google.maps.MapTypeId.ROADMAP,
      scrollwheel : false,
      draggable: false,
      zoom : settings.zoom,
    });
    map.mapTypes.set('map_style', styledMap);
    map.setMapTypeId('map_style');
    
    // Place makers   
    var markers = [];
    $(settings.markers).each(function(index, el) {
      var marker = new google.maps.Marker({ map: map, position: new google.maps.LatLng($(el).attr("data-lat"), $(el).attr("data-lng")) });
      var popup = new google.maps.InfoWindow({ content: $(el).html() });
      
      google.maps.event.addListener(marker, 'click', function() {
        popup.open(map, marker);
      });
      
      markers.push(marker);
    });

		var cluster = new MarkerClusterer(map, markers);
    
    // If we recenter on the makers
    if (settings.recenter == 'markers') {
      var bounds = new google.maps.LatLngBounds();
      jQuery.each(markers, function(index, marker) {
        bounds.extend(marker.getPosition());
      });
      map.fitBounds(bounds);
    }
    if (settings.recenter == 'marker') {
      var bounds = new google.maps.LatLngBounds();
      jQuery.each(markers, function(index, marker) {
        bounds.extend(marker.getPosition());
      });
      map.fitBounds(bounds);
    }
  });
};