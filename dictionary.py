tt={'Monday' :
        {'h1' :
            {'Subject' : 'maths' ,
	            'Teacher' : 'lulu' ,
	            'Room no' : '14'
            }
        },
	 'Tuesday' :
	   {'h2' :
	        {'Subject' : 'statics' ,
	            'Teacher' : 'nazrin mam' ,
	            'Room no' : '15'
	       	}
	   }
	  'wednesday' :
	    {'h3' :
	        {'subject' :'cs' ,
	            'teacher' : 'ds' ,
	            'room no' : '16' 
	        }
	    }       
    }
print(tt['Monday']['h1']['Subject'])
print(tt['Tuesday']['h2']['Subject'])
print(tt['wednesday']['h3']['Subject'])