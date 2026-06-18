import { createRouter, createWebHistory } from 'vue-router'

import DashboardView from '../views/DashboardView.vue'

import AgreementWizardView from '../views/AgreementWizardView.vue'

import AgreementListView from '../views/AgreementListView.vue'

import AgreementDetailView from '../views/AgreementDetailView.vue'

import EditAgreementView from '../views/EditAgreementView.vue'

const router = createRouter({
  history: createWebHistory(),

  routes: [
    {
      path: '/',

      name: 'dashboard',

      component: DashboardView,
    },

    {
      path: '/agreement/new',

      name: 'agreement-new',

      component: AgreementWizardView,
    },

    {
      path: '/agreements',

      name: 'agreements',

      component: AgreementListView,
    },
    {
      path: '/agreements/:id',

      name: 'agreement-detail',

      component: AgreementDetailView,
    },
    {
      path: '/agreements/:id/edit',

      name: 'agreement-edit',

      component: EditAgreementView,
    },
  ],
})

export default router
