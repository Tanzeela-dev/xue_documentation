<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml-stylesheet type="text/xsl" href="OpenGeoSysGLI.xsl"?>

<OpenGeoSysGLI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ogs="http://www.opengeosys.org">
    <name>geometry</name>
    <points>
        <point id="0" x="0" y="10" z="0"/>
        <point id="1" x="0" y="30" z="0"/>
		<point id="2" x="0" y="40" z="0"/>
        <point id="3" x="0" y="60" z="0"/>
		<point id="4" x="0" y="70" z="0"/>
        <point id="5" x="0" y="90" z="0"/>		
        <point id="6" x="100" y="0" z="0"/>
        <point id="7" x="100" y="100" z="0"/>
    </points>
    <polylines>
        <polyline id="0" name="left1">
            <pnt>0</pnt>
            <pnt>1</pnt>
        </polyline>
        <polyline id="1" name="left2">
            <pnt>2</pnt>
            <pnt>3</pnt>
        </polyline>
        <polyline id="2" name="left3">
            <pnt>4</pnt>
            <pnt>5</pnt>
        </polyline>		
        <polyline id="3" name="right">
            <pnt>6</pnt>
            <pnt>7</pnt>
        </polyline>
    </polylines>
</OpenGeoSysGLI>
