(function() {
  var width = 360,
      height = 400;

  var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

  var projection = d3.geo.albers()
    //.center([3.5, 52.6])
    .center([4.3, 52.12])
    .rotate([4.4, 0])
    .parallels([50, 60])
    .scale(75000);
    // .translate([width / 2, height / 2]);

  var path = d3.geo.path()
    .projection(projection);

  var color = d3.scale.linear()
    .domain([0.5, 0.9])
    .range(["red", "green"]);

  
  var deprivationScale = d3.scale.linear()
    .range([1, 5]);

  var sidebar = d3.select('body').append('table').attr('class', 'sidebar');
  
  function updateSidebar(d) {
    var listItems = sidebar.selectAll('tr').data(_.pairs(d.properties));
    var newLi = listItems.enter().append('tr');
    newLi.append('th');
    newLi.append('td');
    listItems.select('th').text(function (d) { return d[0]; });
    listItems.select('td').text(function (d) { return d[1]; });
  }

  d3.json("output/bedford.json", function(error, postcodes) {
    if (error) return console.error(error);
    console.log(path.centroid(topojson.feature(postcodes, postcodes.objects.sectors)));
    console.log(d3.geo.centroid(topojson.feature(postcodes, postcodes.objects.sectors)));

    var features = topojson.feature(postcodes, postcodes.objects.sectors).features;
    
    deprivationScale.domain([
      _.min(_.map(features, function (sector) {
        return sector.properties.IMD;
      })),
      _.max(_.map(features, function (sector) {
        return sector.properties.IMD;
      }))]);
    
    var sectorEls = svg.attr('style', 'background: red').selectAll('.sector')
      .data(features);
    
    sectorEls.enter().append('path')
      .attr('class', function (d) {
        return 'sector ' + d.properties.name.replace(' ','');
      })
      .attr('fill', function (d, i) {
        // Coour according to broadband penetration
        return color(d.properties.connections/d.properties.households);
      })
      .attr('stroke', 'white')
      .on('mouseover', function (d) {
        updateSidebar(d);
      })
      .on('click', function (d) {
        console.log(d.properties.connections/d.properties.households);
        console.log(d.properties.name);
      });
    
        
    
    
    sectorEls.attr("d", path);

    
    // var labelEls = svg.attr('style', 'background: red').selectAll('.label')
    //   .data(features);
    
    // labelEls.enter().append('text');
    // labelEls
    //   .attr('class', 'label')
    //   .attr('dx', function (d) {
    //     return path.centroid(d)[0];
    //   })
    //   .attr('dy', function (d) {
    //     return path.centroid(d)[1];
    //   })
    //   .attr('text-anchor', 'middle');
    //   .text(function (d) { return d.properties.people; });
    

    var dataEls = svg.attr('style', 'background: red').selectAll('.databubble')
      .data(features);
    
    dataEls.enter().append('circle');
    dataEls
      .attr('class', 'databubble')
      .attr('cx', function (d) {
        return path.centroid(d)[0];
      })
      .attr('cy', function (d) {
        return path.centroid(d)[1];
      })
      .attr('r', function (d) {
        return deprivationScale(d.properties.IMD);
      })
      .attr('fill', 'yellow');

  });
})();
