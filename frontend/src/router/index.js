import { createRouter, createWebHistory } from 'vue-router'

import DashboardView from '../views/DashboardView.vue'

import AgreementWizardView from '../views/AgreementWizardView.vue'

const router = createRouter({

history: createWebHistory(),

routes: [

{

path:'/',

name:'dashboard',

component:DashboardView,

},

{

path:'/agreement/new',

name:'agreement-new',

component:AgreementWizardView,

},

],

})

export default router