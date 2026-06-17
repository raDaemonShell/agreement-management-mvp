<template>

<div>

<h2>Step 3: Agreement Details</h2>

<br>

<label>Purpose</label>

<input

v-model="agreementData.purpose"

placeholder="Agreement purpose"

/>

<br><br>

<label>IP Protection</label>

<select v-model="agreementData.ip_protection">

<option value="">

Select

</option>

<option>

Yes

</option>

<option>

No

</option>

</select>

<br><br>

<label>Governing Law</label>

<input

v-model="agreementData.governing_law"

placeholder="Country or State"

/>

<br><br>

<label>Start Date</label>

<input

type="date"

v-model="agreementData.start_date"

/>

<br><br>

<label>End Date</label>

<input

type="date"

v-model="agreementData.end_date"

@change="calculateDuration"

/>

<br><br>

<h3>

Duration:

{{ agreementData.duration }}

days

</h3>

<pre>

{{ agreementData }}

</pre>

</div>

</template>

<script setup>

import { agreementData }

from '../../stores/agreementStore'

function calculateDuration(){

if(

agreementData.start_date

&&

agreementData.end_date

){

const start = new Date(

agreementData.start_date

)

const end = new Date(

agreementData.end_date

)

const difference =

end - start

agreementData.duration =

Math.ceil(

difference /

(1000*60*60*24)

)

}

}

</script>