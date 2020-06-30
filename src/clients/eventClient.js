const request = require('request');
const mainAddr = 'http://localhost:5000';
function parseXml(xml, arrayTags) {
    var dom = null;
    if (window.DOMParser)
    {
        dom = (new DOMParser()).parseFromString(xml, "text/xml");
    }
    // else if (window.ActiveXObject)
    // {
    //     dom = new ActiveXObject('Microsoft.XMLDOM');
    //     dom.async = false;
    //     if (!dom.loadXML(xml))
    //     {
    //         throw dom.parseError.reason + " " + dom.parseError.srcText;
    //     }
    // }
    else
    {
        throw "cannot parse xml string!";
    }

    function isArray(o)
    {
        return Object.prototype.toString.apply(o) === '[object Array]';
    }

    function parseNode(xmlNode, result)
    {
        if (xmlNode.nodeName == "#text") {
            var v = xmlNode.nodeValue;
            if (v.trim()) {
              result['#text'] = v;
            }
            return;
        }

        var jsonNode = {};
        var existing = result[xmlNode.nodeName];
        if(existing)
        {
            if(!isArray(existing))
            {
                result[xmlNode.nodeName] = [existing, jsonNode];
            }
            else
            {
                result[xmlNode.nodeName].push(jsonNode);
            }
        }
        else
        {
            if(arrayTags && arrayTags.indexOf(xmlNode.nodeName) != -1)
            {
                result[xmlNode.nodeName] = [jsonNode];
            }
            else
            {
                result[xmlNode.nodeName] = jsonNode;
            }
        }

        if(xmlNode.attributes)
        {
            var length = xmlNode.attributes.length;
            for(var i = 0; i < length; i++)
            {
                var attribute = xmlNode.attributes[i];
                jsonNode[attribute.nodeName] = attribute.nodeValue;
            }
        }

        var length = xmlNode.childNodes.length;
        for(var i = 0; i < length; i++)
        {
            parseNode(xmlNode.childNodes[i], jsonNode);
        }
    }

    var result = {};
    for (let i = 0; i < dom.childNodes.length; i++)
    {
        parseNode(dom.childNodes[i], result);
    }

    return result;
}
class EventClient {
  
  parseEventFile (filepath) {
    var options = {
      method: 'post',
      body: {directorypath:filepath},
      json: true,
      url: mainAddr + "/parse"
    };
    return new Promise(function (resolve, reject) {
      request(options, (err, res, body) => {
          if (err) { 
            reject(err);  
          }       
          console.log(parseXml(body))
          resolve(body);   

      });
    });
  }

  getFiles (filepath) {
    var options = {
      method: 'post',
      body: {directorypath:filepath},
      json: true,
      url: mainAddr + "/files"
    };
    return new Promise(function (resolve, reject) {
      request(options, (err, res, body) => {
          if (err) { 
            reject(err);  
          }          
          resolve(body);    
      });
    });
  }
}

export default EventClient;  