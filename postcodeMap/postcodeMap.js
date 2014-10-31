(function() {
  var width = 800,
      height = 600;

  var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

  var projection = d3.geo.albers()
    //.center([3.5, 52.6])
    .center([3.8, 52.13])
    .rotate([4.4, 0])
    .parallels([50, 60])
    .scale(75000);
    // .translate([width / 2, height / 2]);

  var path = d3.geo.path()
    .projection(projection);

  var color = d3.scale.linear()
    .range(["red", "green"]);

  d3.json("output/bedford.json", function(error, postcodes) {
    if (error) return console.error(error);
    console.log(path.centroid(topojson.feature(postcodes, postcodes.objects.sectors)));
    console.log(d3.geo.centroid(topojson.feature(postcodes, postcodes.objects.sectors)));
    
    color.domain([0, postcodes.objects.sectors.geometries.length]);

    
    var sectorEls = svg.attr('style', 'background: red').selectAll('.sector')
      .data(topojson.feature(postcodes, postcodes.objects.sectors).features);
    
    sectorEls.enter().append('path')
      .attr('class', function (d) {
        return 'sector ' + d.properties.name.replace(' ','');
      })
      .attr('fill', function (d, i) {
        return color(i);
      })
      .attr('stroke', 'white');
    
    sectorEls.attr("d", path);

    var dataEls = svg.attr('style', 'background: red').selectAll('.databubble')
      .data(topojson.feature(postcodes, postcodes.objects.sectors).features);
    
    dataEls.enter().append('circle');
    dataEls
      .attr('class', 'databubble')
      .attr('cx', function (d) {
        return path.centroid(d)[0];
      })
      .attr('cy', function (d) {
        return path.centroid(d)[1];
      })
      .attr('r', 5)
      .attr('fill', 'red');

  });
})();
