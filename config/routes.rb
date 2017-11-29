Rails.application.routes.draw do
  get 'home/index'

  # post 'shrink', to: 'urls#shrink'
  resources :urls, only: [:create]

  root 'home#index'
end
