Rails.application.routes.draw do
  get 'home/index'

  # Create custom endpoint to /shrinker/shrink
  post 'shrink', to: 'shrinkers#shrink'

  root 'home#index'
end
