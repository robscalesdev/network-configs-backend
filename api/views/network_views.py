from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.network import Network
from ..serializers import NetworkSerializer

# Create your views here.
class NetworksView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = NetworkSerializer
    def get(self, request):
        """Index request"""
        # Get all the mangos:
        # mangos = Mango.objects.all()
        # Filter the mangos by owner, so you can only see your owned mangos
        networks = Network.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = NetworkSerializer(networks, many=True).data
        return Response({ 'networks': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['network']['owner'] = request.user.id
        # Serialize/create mango
        network = NetworkSerializer(data=request.data['network'])
        # If the mango data is valid according to our serializer...
        if network.is_valid():
            # Save the created network & send a response
            network.save()
            return Response({ 'network': network.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(network.errors, status=status.HTTP_400_BAD_REQUEST)

class NetworkDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the mango to show
        network = get_object_or_404(Network, pk=pk)
        # Only want to show owned mangos?
        if request.user != network.owner:
            raise PermissionDenied('Unauthorized, you do not own this mango')

        # Run the data through the serializer so it's formatted
        data = NetworkSerializer(network).data
        return Response({ 'network': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate mango to delete
        network = get_object_or_404(Network, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != network.owner:
            raise PermissionDenied('Unauthorized, you do not own this mango')
        # Only delete if the user owns the  mango
        network.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Mango
        # get_object_or_404 returns a object representation of our Mango
        network = get_object_or_404(Network, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != network.owner:
            raise PermissionDenied('Unauthorized, you do not own this mango')

        # Ensure the owner field is set to the current user's ID
        request.data['network']['owner'] = request.user.id
        # Validate updates with serializer
        data = NetworkSerializer(network, data=request.data['network'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
